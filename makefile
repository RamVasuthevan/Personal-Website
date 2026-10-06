.PHONY: check-rbenv ruby install serve clean

SHELL := /bin/bash

SITE            := website
RUBY_VERSION    := $(shell cat $(SITE)/.ruby-version)
BUNDLER_VERSION := $(shell grep -A1 'BUNDLED WITH' $(SITE)/Gemfile.lock | tail -1 | tr -d ' ')
RBENV           := eval "$$(rbenv init - bash)"

check-rbenv:
	@command -v rbenv >/dev/null || { echo "rbenv not found; install it: https://github.com/rbenv/rbenv#installation"; exit 1; }

ruby: check-rbenv
	rbenv install -s $(RUBY_VERSION)
	cd $(SITE) && $(RBENV) && gem install bundler -v $(BUNDLER_VERSION)

install: ruby
	cd $(SITE) && $(RBENV) && bundle install

serve:
	cd $(SITE) && $(RBENV) && bundle exec jekyll serve --livereload --port 4000

clean:
	cd $(SITE) && rm -rf _site/
