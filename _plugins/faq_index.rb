# Build-time FAQ extraction — no manual generation step.
#
# 1. For each post in the current language, parse `**Q**` + `{:.faq-q}` blocks,
#    inject a stable `id="faq-N"` anchor into the rendered paragraph, and expose
#    the Q/A pairs as `page.faq_items` for the shared FAQPage JSON-LD.
# 2. Build `site.data.faq_index` from App front matter (`faq:`) + parsed posts so
#    /faq/ can render a lightweight question index linking to each answer.
module Jekyll
  module FaqExtractor
    def self.parse(content)
      lines = content.lines
      out = []
      faqs = []
      n = 0
      i = 0
      while i < lines.length
        line = lines[i]
        if line.strip == '{:.faq-q}' && i > 0
          prev = out.last.to_s.strip
          q = if prev.start_with?('**') && prev.end_with?('**') && prev.length > 4
                prev[2..-3]
              elsif prev.start_with?('### ')
                prev.sub(/\A#+\s*/, '')
              end
          if q && !q.empty?
            n += 1
            anchor = "faq-#{n}"
            out << "{:.faq-q ##{anchor}}\n"
            ans = []
            j = i + 1
            while j < lines.length
              break if lines[j].strip == '{:.faq-q}'
              break if lines[j].start_with?('## ')
              nxt = lines[j].strip
              if (nxt.start_with?('**') || nxt.start_with?('###')) && lines[j + 1].to_s.strip == '{:.faq-q}'
                break
              end
              ans << lines[j]
              j += 1
            end
            a = ans.join.strip
            faqs << { 'q' => q, 'a' => a, 'anchor' => anchor } unless a.empty?
            i = j
            next
          end
        end
        out << line
        i += 1
      end
      [faqs, out.join]
    end
  end

  class FaqIndexGenerator < Generator
    priority :high

    def generate(site)
      lang = site.config['lang'] || 'en'

      site.posts.docs.each do |post|
        post_lang = post.data['lang'] || 'en'
        next unless post_lang == lang
        faqs, content = FaqExtractor.parse(post.content.to_s)
        next if faqs.empty?
        post.content = content
        post.data['faq_items'] = faqs
      end

      index = { 'apps' => [], 'posts' => [] }
      app_label = lang == 'en' ? 'apps' : "apps_#{lang}"
      app_coll = site.collections[app_label]
      if app_coll
        app_coll.docs.each do |app|
          items = app.data['faq']
          next if items.nil? || items.empty?
          faqs = items.each_with_index.map do |item, idx|
            { 'q' => item['question'], 'a' => item['answer'], 'anchor' => "faq-#{idx + 1}" }
          end
          index['apps'] << { 'title' => app.data['title'], 'url' => app.url, 'faqs' => faqs }
        end
      end
      site.posts.docs.each do |post|
        faqs = post.data['faq_items']
        next if faqs.nil? || faqs.empty?
        index['posts'] << {
          'title' => post.data['title'], 'url' => post.url,
          'faqs' => faqs.map { |f| { 'q' => f['q'], 'anchor' => f['anchor'] } }
        }
      end
      site.data['faq_index'] = index
    end
  end
end
