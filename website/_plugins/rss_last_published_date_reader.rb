require 'nokogiri'

module Jekyll
  class RSSLastPublishedDate < Generator
    priority :highest

    def generate(site)
      # Load the RSS file
      rss_file_path = File.join(site.source, '_data','kpi','bitsbipsbricks.rss')
      return unless File.exist?(rss_file_path)

      rss_content = File.read(rss_file_path)
      rss = Nokogiri::XML(rss_content)

      # Extract the date time of the last published item
      last_published_date = rss.at_xpath('//item/pubDate').text

      # Make the date time available as a Liquid variable
      site.data['bitsbipsbricks_rss_last_published_date'] = last_published_date
    end
  end
end
