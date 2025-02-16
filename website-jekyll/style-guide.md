---
layout: page
title: Ram's Style Guide
---

This page is a work in progress. But as I polish the sections that already exist, I am adding more rough draft sections. This pushes the page further from being merge-ready and risks leaving it in feature-branch purgatory forever. In theory, I could have feature branches on feature branches, but I don't like that.


## Calendaring

<!-- 
Color Name: Tomato, Hex Code: #D50000
Color Name: Flamingo, Hex Code: #E67C73
Color Name: Tangerine, Hex Code: #F4511E
Color Name: Banana, Hex Code: #F6BF26
Color Name: Sage, Hex Code: #33B679
Color Name: Basil, Hex Code: #0B8043
Color Name: Peacock, Hex Code: #039BE5
Color Name: Blueberry, Hex Code: #3F51B5
Color Name: Lavender, Hex Code: #7986CB
Color Name: Grape, Hex Code: #8E24AA
Color Name: Graphite, Hex Code: #616161
Color Name: Calendar colour, Hex Code: #4285F4
-->

| Type                                                                           | Color     | Notes             | Comment                                              |
|--------------------------------------------------------------------------------|-----------|-------------------|------------------------------------------------------|
| Sleep                                                                          | Graphite  |                   | Good                                                 |
| Social Event                                                                   | Tomato    | With other people | Good                                                 |
| Reminder                                                                       | Tangerine | Zero-length even  | Good                                                 |
| Context Change Errand                                                          | Flamingo  |                   |                                                      |
| No Context Change Errand                                                       | Lavender  |                   |                                                      |
| [Alive Time](https://ryanholiday.net/will-you-choose-alive-time-or-dead-time/) | Gold      |                   |                                                      |
| Employment                                                                     | Sage      |                   |                                                      |
| Outside                                                                        | Flamingo  |                   | Go somewhere without order people but not an errand? |                                                                        |

Regarding errands:

What is `Get Ready for Work` vs `Go to Longos` vs `Workout at home`? Are they all errands? 

I feel like indoor/outdoor errands are different. Or maybe the distinction is between errands which require context/environment changes and ones which don't.  

So `Workout at home` and `Go to Longos` are Context Change Errands, but `Get Ready for Work` is not

This calendaring section does not feel done, but it is probably my personal most visited page. It's annoying to go to the [GitHub pull request](https://github.com/RamVasuthevan/Personal-Website/pull/458), then the [Cloudflare Pages preview](https://style-guide-calendaring.personal-website-a13.pages.dev/), and then [All Pages](https://style-guide-calendaring.personal-website-a13.pages.dev/all-pages) and then [Style Guide](https://style-guide-calendaring.personal-website-a13.pages.dev/style-guide). So, let's just merge it in.

## Dates

- Dates should whenever possible be written YYYY-MM-DD. See [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6) `full-date`

## Python

### Dependency Management
- I almost always use pipenv and PipFile (But maybe I [should](https://til.simonwillison.net/python/pyproject) be using poetry and pyproject.toml)

### Libraries

| Purpose               | Preferred                        |
|-----------------------|----------------------------------|
| Web Scraping          | BS4        |
| HTTP Requests         | requests                         |
| SQLite frontend      | datasette                        |
| SQLite ORM     | sqlite-utils (for simple SQLite) |


## Licence
- I prefer the MIT licence because it is the default permissive licence

