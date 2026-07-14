---
layout: page
title: Google Photos
---

1. Search by exact filename: paste `"PXL_20260709_233247707"` (with quotes) into the search box
    - Quotes force exact-text matching on filenames, captions, and OCR'd text; without quotes results are fuzzy
    - Don't build it as a URL — `photos.google.com/search/%22...%22` mangles underscored filenames on redirect (drops the date segment)

2. Search a whole day: `July 9, 2026` in the search box (or `photos.google.com/search/July%209%2C%202026`)

3. After a search runs, the URL becomes a base64 blob: the query + a timestamp of when you searched — a frozen snapshot that's safe to bookmark

4. Pixel filenames (`PXL_<YYYYMMDD>_<HHMMSS>`) are UTC — evening Toronto photos get the next day's date
