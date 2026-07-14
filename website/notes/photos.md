---
layout: page
title: Google Photos
---

## Links
- [Google Photos Search Documentation](https://support.google.com/photos/answer/15235862)

1. `"PXL_20260709_233247707"`
    - Quotes match exact text in filenames, captions, and text inside photos

2. `photos.google.com/search/<base64 token>`
    - Search URLs are a base64url-encoded protobuf. It holds the query string twice (field 1: the executed query, field 4: the display query shown in the search box), the time the search ran as a millisecond timestamp (field 5), and a search-type enum (field 7)
    - Builds a search URL for any filename:

      ```python
      import base64, time

      def photos_search_url(q):
          def v(n):
              out = b""
              while True:
                  b = n & 0x7F; n >>= 7
                  out += bytes([b | (0x80 if n else 0)])
                  if not n: return out
          def ld(f, p): return bytes([f << 3 | 2]) + v(len(p)) + p
          qb = f'"{q}"'.encode()
          m = ld(1, qb) + ld(4, ld(1, qb)) + b"(" + v(int(time.time() * 1000)) + b"8\x03"
          return "https://photos.google.com/search/" + base64.urlsafe_b64encode(m).decode().rstrip("=")

      print(photos_search_url("PXL_20260709_233247707"))
      ```
