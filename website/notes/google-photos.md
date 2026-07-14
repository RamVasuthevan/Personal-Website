---
layout: page
title: Google Photos
---

1. Search by exact filename: `"PXL_20260709_233247707"`
    - Quotation marks force exact-text matching against filenames, captions, camera models, and text OCR'd inside photos
    - Without quotes the search goes fuzzy/semantic and returns "most relevant" guesses instead
    - There is no `filename:` operator — Google Photos has no Gmail-style operator syntax; quoted text is the whole mechanism

2. Search as a URL: `https://photos.google.com/search/<url-encoded query>`
    - Quoted filename: `https://photos.google.com/search/%22PXL_20260709_233247707%22` (`%22` = quote)
    - Date search: `https://photos.google.com/search/July%209%2C%202026` — natural-language dates work; use this to browse a whole day

3. After a search runs, the address bar rewrites to `photos.google.com/search/<base64 blob>`
    - The blob is base64url-encoded protobuf holding the search state: the query string, a microsecond timestamp of when the search ran, and a search-type enum
    - It's frozen state, not a live query — build shareable/composable searches with the plain-text URL form instead

4. Pixel camera filenames (`PXL_<YYYYMMDD>_<HHMMSSmmm>`) use UTC
    - A photo taken after 8pm in Toronto (EDT) is stamped with the next day's date — check both days when hunting by date
