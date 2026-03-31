.PHONY: install serve clean

SHELL := /bin/bash

install:
	cd website && eval "$$(rbenv init -)" && bundle install

serve:
	cd website && eval "$$(rbenv init -)" && bundle exec jekyll serve --livereload --port 4000

clean:
	cd website && rm -rf _site/