all: test

test:
	flake8 --ignore=E501
	nosetests --with-coverage

.PHONY: all
