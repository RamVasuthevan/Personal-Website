---
layout: page
title: Git Scraping
---

[Git Scraping](https://simonwillison.net/2020/Oct/9/git-scraping/) inspired by Simon Willison. 

Download a file regularly using Git Actions, check it into Git and see how it changes over time.

### Scraping Project
- [Toronto Lobbyist Registry Data](https://github.com/RamVasuthevan/TorontoLobbyistRegistryData)  
    - [Downloads](https://github.com/RamVasuthevan/TorontoLobbyistRegistry/blob/main/.github/workflows/scrape.yml) data from [City of Toronto Lobbyist Registry](https://open.toronto.ca/dataset/lobbyist-registry/)
    - The files here are quite large, so they need to be stored in Git LFS, so Github Git Blame does not work
    - A part of my [Lobbying in Toronto](https://github.com/RamVasuthevan/TorontoLobbyistRegistry) project
- [City of Toronto Competitive Contracts Data](https://github.com/RamVasuthevan/city-of-toronto-contracts-data)  
    - [Downloads](https://github.com/RamVasuthevan/city-of-toronto-contracts-data/blob/main/.github/workflows/scrape.yml) data about [Competitive Contracts](https://open.toronto.ca/dataset/competitive-call-award-results/), [Non Competitive Contracts](https://open.toronto.ca/dataset/non-competitive-contracts/) and [Solicitations for the Purchase of Goods and Services](https://open.toronto.ca/dataset/call-documents-for-the-purchase-of-goods-and-services/) issued by the City of Toronto
- [Ontario Marriage Officiants](https://github.com/RamVasuthevan/ontario-marriage-officiants)
    - [Downloads](https://github.com/RamVasuthevan/ontario-marriage-officiants/blob/main/.github/workflows/scrape.yml) list of [registered marriage officiants](https://data.ontario.ca/dataset/38ddc983-1bf0-4bee-ad18-07dac8cfe884/resource/e010f610-c3d6-4f88-849b-6f8c11e98d9c/) in Onatrio