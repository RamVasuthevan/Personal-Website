---
layout: page
title: Google Photos
---

## Links
- [Search by people, things & places in your photos](https://support.google.com/photos/answer/15235862)

1. `"PXL_20260709_233247707"`
    - Exact filename search — paste into the search box, quotes included
    - Quotes force exact-text matching on filenames, captions, and OCR'd text; without quotes results are fuzzy
    - Typing it as a URL (`photos.google.com/search/%22...%22`) does not work — the redirect mangles underscored filenames (drops the date segment)

2. `July 9, 2026`
    - Date search — works in the search box and as a URL: `photos.google.com/search/July%209%2C%202026`

3. `photos.google.com/search/<base64 token>`
    - What the URL becomes after a search runs: base64url-encoded protobuf of the query plus a timestamp — a frozen snapshot, safe to bookmark
    - A working URL for any filename can be minted by building the token:

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

4. `PXL_<YYYYMMDD>_<HHMMSS>` filenames are UTC
    - An evening photo in Toronto is stamped with the next day's date
