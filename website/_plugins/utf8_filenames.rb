# Cloudflare Pages builds without a UTF-8 locale, which breaks non-ASCII filenames.
Encoding.default_external = Encoding::UTF_8
