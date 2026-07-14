---
layout: page
title: Google Photos
---

## Links
- [Google Photos Search Documentation](https://support.google.com/photos/answer/15235862)

## Notes

1. Search for images by filename
    - Quotes match exact text in filenames, captions, and text inside photos
    - eg `"PXL_20260709_233247707.jpg"` or `"PXL_20260709"` or `"Fnu thanked you for your Tip"`

2. Build a Google Photos search URL
    - Search URLs are a base64url-encoded protobuf holding:
        - field 1: the executed query
        - field 4: the display query shown in the search box (same string as field 1)
        - field 5: the time the search ran, as a millisecond timestamp
        - field 7: a search-type enum
    - eg `photos.google.com/search/<base64 token>`
    - Build a search URL for any filename:

      ```python
      import base64
      import time

      WIRE_VARINT = 0
      WIRE_LEN = 2  # length-delimited: strings, bytes, nested messages

      def encode_varint(value: int) -> bytes:
          # 7 bits per byte, least-significant group first; high bit = more follows
          out = bytearray()
          while True:
              byte = value & 0x7F
              value >>= 7
              if value:
                  out.append(byte | 0x80)
              else:
                  out.append(byte)
                  return bytes(out)

      def encode_tag(field_number: int, wire_type: int) -> bytes:
          return encode_varint((field_number << 3) | wire_type)

      def encode_len_field(field_number: int, payload: bytes) -> bytes:
          return encode_tag(field_number, WIRE_LEN) + encode_varint(len(payload)) + payload

      def encode_varint_field(field_number: int, value: int) -> bytes:
          return encode_tag(field_number, WIRE_VARINT) + encode_varint(value)

      def photos_search_url(q: str) -> str:
          query = f'"{q}"'.encode()  # quotes are search syntax: exact match
          message = (
              encode_len_field(1, query)                         # executed query
              + encode_len_field(4, encode_len_field(1, query))  # display query
              + encode_varint_field(5, int(time.time() * 1000))  # timestamp (ms)
              + encode_varint_field(7, 3)                        # search-type enum
          )
          token = base64.urlsafe_b64encode(message).decode().rstrip("=")
          return "https://photos.google.com/search/" + token

      print(photos_search_url("PXL_20260709_233247707"))
      ```
