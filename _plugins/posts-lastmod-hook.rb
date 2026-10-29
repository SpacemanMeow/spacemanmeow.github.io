#!/usr/bin/env ruby
#
# Git-driven, build-stable dates for posts and collection documents (apps):
#   - last_modified_at: last commit that touched the file (fallback: file mtime)
#   - date:             first commit that added the file   (fallback: file mtime)
#     Only for collection documents lacking a front-matter date; posts already
#     derive their date from the filename.
# All values are computed at BUILD time and stored only in memory — source
# files are never written back, so committing can never trigger new file
# changes. Without the `date` fix-up below, Jekyll falls back to `site.time`
# for collection documents, which made `article:published_time` /
# `article:modified_time` churn on every rebuild.

require "time"

Jekyll::Hooks.register [:posts, :documents], :post_init do |doc|
  path = doc.path

  fallback = begin
    File.mtime(path).iso8601
  rescue StandardError
    next
  end

  lastmod = `git log -1 --pretty="%aI" -- "#{path}"`.strip
  lm = lastmod.empty? ? fallback : lastmod
  begin
    doc.data["last_modified_at"] = Time.parse(lm)
  rescue StandardError
    doc.data["last_modified_at"] = lm
  end

  unless doc.collection.label == "posts"
    created = `git log --pretty="%aI" -- "#{path}"`.lines
              .map(&:strip).reject(&:empty?).last
    pub = created || fallback
    begin
      doc.data["date"] ||= Time.parse(pub)
    rescue StandardError
      doc.data["date"] ||= pub
    end
  end
end
