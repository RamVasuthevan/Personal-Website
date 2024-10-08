----
layout: page
title: Build ckan-to-sqlite
---

I want to build ckan-to-sqlite, with downloads information about an ckan instance and puts into into a sqlite db, so that I can search it in Datasette.

I want to build this because so that I can search for datasets on [Toronto Open Data portal](https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/) which have csv but not shp file, ie not geographical data. I can search datasets with have a csv file but I can't search for datasets which don't have a shp file.

I am at an interesting time in my engineering journey. I watched [this](https://www.youtube.com/watch?v=mTa2d3OLXhg) interview by DHH on the ThePrimeTimeagen. And I realized that I have a fear of servers. Working on getting more comfortable for deploying and maintaining servers. My main IDE used to be VS Code/Cursor. I'm getting a bit frustrated with it because not fast, it's a bit too heavyweight and I want more control over how I work. I'm trying to used to vim to edit files as much as possible, although sometimes it is frustrating so I use Sublime. Eventually, I want to migrate to a full neovim IDE.

Since I've been playing around with cli tools, I've been really impressed with [sqlite-utils](https://github.com/simonw/sqlite-utils), [jq]() and [nu] shell.

I really like the ideas behind [Dogsheep](https://dogsheep.github.io/), I really want to write some library to extract data out service which I use. But before I do that, I want to get started by building a simple tool with well struced data. And unlike some other scraping projects, where you need to compliced scripts or are afraid of accidentally DDOSing the sites, I think these CKAN istances will be fine with a couple dozen api calls.

CLI API:
ckan-to-sqlite toronto-open-data.db https://ckan0.cf.opendata.inter.prod-toronto.ca

Endpoints I want to download:
- status_show
- tag_list
- group_list
- package_list
- organization_list
- current_package_list_with_resources


Base Urls for CKAN Instance:
 - [City of Toronto Open Data](https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/)
 - [Ontario Open Data](https://data.ontario.ca/api/3/action/)
 - [Canada](https://open.canada.ca/data/en/api/3/action/)
 
Read More:
- [CKAN Instance Analysis](https://civicdataecosystem.org/2023/06/19/analysis.html)
- [CKAN API guide](https://docs.ckan.org/en/2.9/api/)