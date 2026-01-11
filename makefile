.PHONY: install serve build clean

SHELL := /bin/bash

install:
	cd website && eval "$$(rbenv init -)" && bundle install

serve:
	cd website && eval "$$(rbenv init -)" && bundle exec jekyll serve --livereload --port 4000

build:
	cd website && bundle exec jekyll build

clean:
	cd website && rm -rf _site/