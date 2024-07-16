---
layout: page
title: What I am Thinking About?
---

# A Select Statement View of Toronto 
How is the city viewed from the perspective of a database ([Seeing like a state](https://slatestarcodex.com/2017/03/16/book-review-seeing-like-a-state/)):
- Government
	- POLARIS (Province of Ontario Land Registration Information System) is the Electronic Land Registration System (ELRS) for Ontario, managed by Terranet, a portfolio company of OMERS (Ontario Municipal Employees Retirement System), the pension fund for municipal workers 😂
    - MPAC (Municipal Property Assessment Corporation), a crown corporation, determines the assessed value of all the properties in Ontario so that property taxes can be calculated
    - What is the relationship between the various branches of the government and Terranet?
    - How was Terranet created? How was POLRIAS created? How was MPAC created?
    - How were things done before POLRIAS? And digitization?
    - How is the POLARIS structured from a technical perspective?
    - Who are their customers? How do they use it? Can I use this data?

- Realtors
    - TRREB is the professional association for real estate brokers and salespeople in the GTA, which manages the Toronto MLS (Multiple Listing Service) system
    - What actually is MLS? What is the relationship between Toronto MLS and other MLS systems? 
    - TRREB vs. Competition Bureau and TRREB vs Mongohouse (scraping)
    - How do realtors, their customers and the public gain access to this data? Both from a legal and technical perspective?
    - How can I get access to the data?

- Other?
	- Are there other DBs that have an interesting view on the city?
	- Are there opportunities for creating interesting DBs?
	- With the data which exists, what new view on real estate development can be built?
	- Here are some other views on Toronto
		- [City of Toronto Open Data](https://open.toronto.ca/catalogue/?search=development&sort=score%20desc)
		- [Urban Toronto Projects DB](https://urbantoronto.ca/database/projects/)
		- [Future Model Toronto](https://www.stephenvelasco.com/)
        - [TORONTOVERSE](https://torontoverse.com/)

# Interesting Land Tenure, Zoning and Municipal Governance
- Across Canada and the United States there's a lot of uniformity in the relationship between municipal governments, land and its uses but there are some interesting anomalies: <!-- (TODO add a explain for why these are interesting) -->
    - UBC University Endowment Lands
    - Reedy Creek Improvement District
    - Universal City
    - City of Industry
    - The Villages
    - Loudoun County
    - Mobile City (Texas)
    - Houston
    - Sen̓áḵw
    - (The canceled) Sidewalk Toronto
    - Leasehold condominiums in Vancouver
    - Public Facility Corporations in Texas
    - Towns associated with religious groups (Ave Maria FL, Antelope OR, Kiryas Joel NY, Lakewood NJ)
    - Paradise, Nevada
    - Ward’s Island and Algonquin Island in Toronto
    - Rosemont, Illinois <!--  https://twitter.com/north0fnorth/status/1713960831602323613 -->
    - Free Acres, New Jersey <!-- https://twitter.com/mnolangray/status/1650599822972567552?t=KctJuMsesHDRh9-Z9VS8CQ&s=19 https://www.nj.com/inside-jersey/2014/09/hidden_jersey_were_off_to_see_free_acres.html -->
    -  Rosemont, Illinois <!--  https://x.com/north0fnorth/status/1713960831602323613?s=20 -->
    
# Get more from data
- There are massive amounts of data which is being explicitly and implicitly created
- It is being constantly pumped out into the void, being forgotten, lost and overwritten
- It’s sitting there waiting to be parsed, structured, cleaned, searched and visualized. To be made useful
- We have created great tools for sharing open-source code (Git, Github, PyPI, etc.), but how do we share open data?
- We have created easy-to-use tools for sharing documents (Google Drive, Jekyll, Cloudflare Pages, etc.), but what about indexing, searching and visualizing data?
See:
- [Git scraping: track changes over time by scraping to a Git repository](https://simonwillison.net/2020/Oct/9/git-scraping/)
- [The Magic of Small Databases](https://tomcritchlow.com/2023/01/27/small-databases/)
- [Bloomberg Terminal for everything](https://marginalrevolution.com/marginalrevolution/2019/12/work-on-these-things.html#:~:text=Bloomberg%20Terminal%20for,variety%20of%20domains.)
- [Lobbying in Toronto](https://github.com/RamVasuthevan/TorontoLobbyistRegistry/)

# Building perpetual websites
- The web is an evolving standard. A website that works today can break tomorrow because a browser vendor decides not to honour a standard
- How do you build websites that last forever? Not years, but decades
- It’s sad to see projects in which people put blood, sweat and tears (okay, probably not blood) break. It’s sad to see linkrot slowly, deteriorate away the web
- Initial Ideas:
    - Static site generators
    - HTML/CSS only websites
    - Store in a public repo and host on Github Pages
    - Save all links to the Internet Archive
    - 10 year domain registration

# Paradigms for one-person software projects
- For example, if a 1000 people are working on a project, breaking that project up into microservices and multiple repos could reduce the amount of coordination needed. But if only one person is working on the project, that might add unnecessary complexity
- How should a project be structured differently if the project manager, designer, marketer and engineer are the same person?

# Startup of you
- There's advice for portfolio management and career management
- There isn’t much personal finance advice that acknowledges that most people’s largest asset is human capital
