all: test

test:
	flake8
	nosetests --with-coverage

.PHONY: all
