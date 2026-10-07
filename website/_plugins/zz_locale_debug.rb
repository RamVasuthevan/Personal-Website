# Temporary: report the build machine's locale. Not for merging.
report = <<~TXT
  LANG=#{ENV["LANG"].inspect}
  LC_ALL=#{ENV["LC_ALL"].inspect}
  LC_CTYPE=#{ENV["LC_CTYPE"].inspect}
  ruby=#{RUBY_VERSION}
  Encoding.locale_charmap=#{Encoding.locale_charmap}
  Encoding.find("locale")=#{Encoding.find("locale")}
  --- locale
  #{`locale 2>&1`.gsub("\n", "\n  ")}
  --- locale -a
  #{`locale -a 2>&1`.lines.first(12).join.gsub("\n", "\n  ")}
  --- os
  #{`(grep PRETTY_NAME /etc/os-release || sw_vers) 2>&1`.gsub("\n", "\n  ")}
TXT
puts "LOCALE-DEBUG-BEGIN", report, "LOCALE-DEBUG-END"
Jekyll::Hooks.register(:site, :post_write) do |site|
  File.write(File.join(site.dest, "locale-debug.txt"), report)
end
