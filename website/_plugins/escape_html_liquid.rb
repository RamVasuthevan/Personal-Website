module Jekyll
  class RenderFileTag < Liquid::Tag

    def initialize(tag_name, file, tokens)
      super
      @file = file.strip
    end

    def render(context)
      file_path = File.join(context.registers[:site].source, '_includes', @file)
      return "File not found: #{@file}" unless File.exist?(file_path)

      file_content = File.read(file_path)
      # The following line marks the content as "safe", preventing automatic escaping
      file_content = file_content.force_encoding("UTF-8")
      # Ensure content is not auto-escaped by marking as HTML safe (Jekyll 4+)
      if file_content.respond_to?(:html_safe)
        file_content.html_safe
      else
        file_content
      end
    end
  end
end

Liquid::Template.register_tag('render_file', Jekyll::RenderFileTag)
