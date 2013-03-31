.PHONY: build

ifndef VTENV_OPTS
VTENV_OPTS = "--no-site-packages"
endif

build:	
	mkdir -p $(PIP_DOWNLOAD_CACHE)
	virtualenv $(VTENV_OPTS) .
	bin/pip install zope.pagetemplate
	bin/pip install numpy
	bin/pip install pandas
	bin/pip install mr.bob
