---
layout: page
title: Nushell
---

[Nushell](https://www.nushell.sh/) is a new shell built around data instead of text

I learned about [Nushell](https://www.nushell.sh/) from this video from [Tom Delalande](https://www.youtube.com/watch?v=K_yK-tEeGDA). I was blown away by how good it was at interrogating data.

## Notes:
- [from json --objects](https://www.nushell.sh/commands/docs/from_json.html) parses JSONL, treating each line as a separate JSON object (e.g. `open data.json | from json --objects`)
- [table --expand](https://www.nushell.sh/commands/docs/table.html) renders nested records inline instead of collapsing them to `{record 1 field}`
- [explore](https://www.nushell.sh/book/explore.html) is a pager like [less](https://en.wikipedia.org/wiki/Less_(Unix)) but for tables in nushell


## Useful commands
- sort-by
- reverse
- where
- first
- get


## References:
- [Nushell Book](https://www.nushell.sh/book/)
- [Command Reference](http://nushell.sh/commands/)
- [Quick Tour — Nushell](https://www.nushell.sh/book/quick_tour.html)
