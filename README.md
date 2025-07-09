# Personal-Website

  

Created a simple personal website.
Inspired using by [Tweet](https://twitter.com/everestpipkin/status/1588636275942502400?s=20&t=ugmG3OLXRUIKGov6VA4zEQ).

- Developing using Github Codespaces
- Deploying the website using Cloudflare Pages
- Using [The Baked Data pattern](https://simonwillison.net/2021/Jul/28/baked-data/)

Everything required to build site should be in this repo

No db. Manually editing files. Deploying the website using Cloudflare Pages.

### TODO:

1. Think about how to archive articles. WIP - [PrivateLibrary](https://github.com/RamVasuthevan/PrivateLibrary)
2. Make pretty
3. Start vendoring dependencies 


### CloudFlare Pages Env Variables 

#### Production
- RUBY_VERSION=3.2.2

#### Preview
- RUBY_VERSION=3.2.2


## How to Run
```fish
eval "$(rbenv init -)"
bundle install
bundle exec jekyll serve --livereload --port 4000
```

(See [this](https://chatgpt.com/c/67871672-aec8-8013-b80d-78d0e6ca6a75))

## Photo of the Day

- 2024-07-04 and before are good for Photo of the Day