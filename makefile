.PHONY: ruby install serve clean

SHELL := /bin/bash
RBENV := eval "$$(rbenv init - bash)"

ruby:
	@command -v rbenv >/dev/null || { echo "rbenv not found; install it: https://github.com/rbenv/rbenv#installation"; exit 1; }
	cd website && rbenv install -s
	cd website && $(RBENV) && gem install bundler -v "$$(awk '/BUNDLED WITH/{getline; print $$1}' Gemfile.lock)"

install: ruby
	cd website && $(RBENV) && bundle install

serve:
	cd website && $(RBENV) && bundle exec jekyll serve --livereload --port 4000

clean:
	cd website && rm -rf _site/
