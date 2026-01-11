.PHONY: install serve clean

SHELL := /bin/bash

install:
	eval "$$(rbenv init -)" && bundle install

serve:
	eval "$$(rbenv init -)" && bundle exec jekyll serve --livereload --port 4000

clean:
	rm -rf _site/