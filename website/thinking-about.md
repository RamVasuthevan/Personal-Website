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
    - How was Terranet created? How was POLARIS created? How was MPAC created?
    - How were things done before POLARIS? And digitization?
    - How is POLARIS structured from a technical perspective?
    - Who are their customers? How do they use it? Can I use this data?

- Realtors
    - TRREB is the professional association for real estate brokers and salespeople in the GTA, which manages the Toronto MLS (Multiple Listing Service) system
    - What actually is MLS? What is the relationship between Toronto MLS and other MLS systems? 
    - TRREB vs. Competition Bureau and TRREB vs Mongohouse (scraping)
    - How do realtors, their customers and the public gain access to this data? Both from a legal and technical perspective?
    - How can I get access to the data?

- Other
	- Are there other DBs that have interesting views of the city?
	- Are there opportunities to create interesting DBs?
	- With the existing data, what new views on real estate can be built?
	- Here are some other views on Toronto
		- [City of Toronto Open Data](https://open.toronto.ca/catalogue/?search=development&sort=score%20desc)
		- [Urban Toronto Projects DB](https://urbantoronto.ca/database/projects/)
		- [Future Model Toronto](https://www.stephenvelasco.com/)
        - [TORONTOVERSE](https://torontoverse.com/)

# Interesting Land Tenure, Zoning and Municipal Governance
- Across Canada and the United States, there's a lot of uniformity in the relationship between municipal governments and land use, but there are some interesting anomalies: 
I'll add a "Why Notable" column explaining what makes each location interesting from a governance/development perspective:

| Location | Why Notable |
|----------|-------------|
| [UBC University Endowment Lands](https://en.wikipedia.org/wiki/University_Endowment_Lands)| Special administrative district managed by BC government and UBC. UBC owns the land and controls the zoning. They have developed some of the land and sold leasehold condominiums|
| [Reedy Creek Improvement District](https://en.wikipedia.org/wiki/Reedy_Creek_Improvement_Act) | A special-purpose taxing district which has the same powers as a county government, controled by Disney overseeing the land around Disney World|
| [Universal City](https://en.wikipedia.org/wiki/Universal_City,_California) | Is an unincorporated area in LA County, owned mainly by Universal Pictures. Universal Studio directly integrates with the different levels of the government, and provides some the services normally provided by municipalities. |
| [City of Industry](https://en.wikipedia.org/wiki/City_of_Industry,_California) | Almost all of the city is industrial and commercial. See [Youtube Video())|
| The Villages | Massive retirement community in Florida with special district powers and unique governance |
| Loudoun County | Data center hub with special zoning/tax arrangements, making it critical to global internet infrastructure |
| Mobile City (Texas) | Tiny municipality (~200 people) known for permissive adult business regulations |
| Houston | Largest U.S. city without traditional zoning laws, uses deed restrictions instead |
| Sen̓áḵw | First Nations development on reserve land in Vancouver, exempt from city planning rules |
| (The canceled) Sidewalk Toronto | Failed "smart city" project by Google's Sidewalk Labs that raised governance questions |
| Leasehold condominiums in Vancouver | Property ownership structure where land is leased long-term, common in Vancouver |
| Public Facility Corporations in Texas | Special non-profit entities that can provide property tax exemptions for housing |
| Towns associated with religious groups | Communities effectively controlled by religious groups through voting/governance |
| Paradise, Nevada | Unincorporated area containing Las Vegas Strip, governed by Clark County not City of Las Vegas |
| Ward's Island and Algonquin Island in Toronto | Land trust communities with unique lease structure and governance |
| Rosemont, Illinois | Village heavily dependent on convention/entertainment revenue, unusual governance structure |
| Free Acres, New Jersey | Historic land trust community founded on Georgist single-tax principles |
    
# Get more from data
- There are massive amounts of data which is being explicitly and implicitly created
- It is being constantly pumped out into the void, being forgotten, lost and overwritten
- It’s sitting there waiting to be saved, parsed, structured, cleaned, searched and visualized. To be made useful
- We have created great tools for sharing open-source code (Git, Github, PyPI, etc.), but how do we share open data?
- We have created easy-to-use tools for sharing documents (Google Drive, Jekyll, Cloudflare Pages, etc.), but what about indexing, searching and visualizing data?
- See:
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
    - Store in a public Github repo and host on GitHub Pages
    - Save all links to the Internet Archive
    - 10 year domain registration

# Paradigms for one-person software projects
- For example, if 1000 people are working on a project, breaking that project up into microservices and multiple repos could reduce the coordination needed. But if only one person is working on the project, that might add unnecessary complexity
- How should a project be structured differently if the project manager, designer, marketer and engineer are the same person?

# Startup of you
- There's a lot of advice for investment portfolio management, career development, and personal finance
- There isn't much personal finance advice that acknowledges that most people's largest asset is the present value of expected future earnings