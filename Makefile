all: test

test:
	flake8 --ignore=E501
	nosetests --logging-config logging_config.ini --nocapture --with-coverage --cover-package=cxc_toolkit

.PHONY: all
