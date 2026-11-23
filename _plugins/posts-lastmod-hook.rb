#!/usr/bin/env ruby
#
# Git-driven, build-stable dates for posts and collection documents (apps):
#   - last_modified_at: last commit that touched the file (fallback: file mtime)
#   - date:             first commit that added the file   (fallback: file mtime)
#     Only for collection documents lacking a front-matter date; posts already
#     derive their date from the filename.
# All values are computed at BUILD time and stored only in memory — source
# files are never written back, so committing can never trigger new file
# changes. Without the date fix-up below, Jekyll falls back to `site.time`
# for collection documents, which made `article:published_time` /
# `article:modified_time` churn on every rebuild.

require "time"
require "shellwords"

DATE_MARK = "__DATE__"

# One `git log` pass for the whole repo instead of one subprocess per document.
# Newest-first order: first hit = last commit, last hit = first commit.
def git_date_maps
  last, first = {}, {}
  current = nil
  `git log --pretty=tformat:#{DATE_MARK}%aI --name-only`.each_line do |line|
    line = line.chomp
    if line.start_with?(DATE_MARK)
      current = line[DATE_MARK.length..]
    elsif !line.empty?
      last[line] ||= current
      first[line] = current
    end
  end
  [last, first]
end

$git_last, $git_first = nil, nil

def git_dates_for(path)
  $git_last, $git_first = git_date_maps if $git_last.nil?
  return [$git_last[path], $git_first[path]] if $git_last.key?(path)

  # Untracked files or paths git reports differently: scoped fallback.
  # Shellwords.escape keeps spaces/quotes in a path from breaking the command.
  safe = Shellwords.escape(path)
  lm = `git log -1 --pretty="%aI" -- #{safe}`.strip
  cr = `git log --pretty="%aI" -- #{safe}`.lines.map(&:strip).reject(&:empty?).last
  [lm.empty? ? nil : lm, cr]
end

def parse_time(value, fallback)
  return fallback if value.nil? || value.empty?
  Time.parse(value)
rescue StandardError
  fallback
end

# :documents is intentional: apps (11 x 5 languages) carry no front-matter
# `date`, so their lastmod/date would fall back to site.time and churn on
# every rebuild. Registering only :posts would break that — see D8.
Jekyll::Hooks.register [:posts, :documents], :post_init do |doc|
  fallback = begin
    File.mtime(doc.path).iso8601
  rescue StandardError
    next
  end

  last, created = git_dates_for(doc.path)
  doc.data["last_modified_at"] ||= parse_time(last, fallback)

  unless doc.collection.label == "posts"
    doc.data["date"] ||= parse_time(created, fallback)
  end
end
