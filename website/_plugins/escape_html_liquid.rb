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
        CGI.escapeHTML(file_content)
      end
    end
  end
  
  Liquid::Template.register_tag('render_file', Jekyll::RenderFileTag)
  