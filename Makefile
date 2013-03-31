.PHONY: docs build test coverage pylint flake8 pep8 pyflakes templer diff sloccount dryrelease mkrelease

ifndef VTENV_OPTS
VTENV_OPTS = "--no-site-packages"
endif

docs: bin/sphinx-build
	SPHINXBUILD=../bin/sphinx-build $(MAKE) -C docs html $^

build:	
	virtualenv $(VTENV_OPTS) .
	mkdir -p $(PIP_DOWNLOAD_CACHE)
	virtualenv $(VTENV_OPTS) .
	bin/pip install zope.pagetemplate
	bin/pip install numpy
	bin/pip install pandas
	bin/pip install mr.bob
	bin/pip install pandas
	if [ -d src/pigeonhole ]; then cd src/pigeonhole; git pull; fi 
	if [ ! -d src/pigeonhole ]; then git clone git@github.com:maikroeder/pigeonhole.git src/pigeonhole; fi 	
	bin/pip install -U src/pigeonhole
	bin/python setup.py develop

test: bin/nosetests
	bin/nosetests -s encode/mouse

coverage: bin/coverage bin/nosetests
	bin/nosetests --with-coverage --cover-html --cover-html-dir=html --cover-package=encode.mouse
	bin/coverage html

pylint:	bin/pylint
	bin/pylint -i y encode/mouse

flake8:	bin/flake8
	bin/flake8 --max-complexity 12 encode/mouse

pep8:	bin/pep8
	bin/pep8 encode/mouse

pyflakes:	bin/pyflakes
	bin/pyflakes encode/mouse

templer: bin/python
	# Hack to make believe templer that the current folder is the home folder
	# so that it reads the local .zopeskel file with the defaults
	export OLDHOME="${HOME}"; export HOME="${PWD}"; ./bin/templer dotpackage encode.mouse; export HOME="${OLDHOME}"

diff: bin/python
	# Show the difference between the current package and the regenerated one
	colordiff -c -r encode.mouse .|less -r

sloccount:	bin/python
	sloccount encode/mouse

dryrelease:	bin/mkrelease
	bin/mkrelease --no-commit --no-tag --dry-run -d pypi

mkrelease:	bin/mkrelease
	bin/mkrelease --no-commit --no-tag  -d pypi

bin/sphinx-build: bin/python
	bin/pip install sphinx
	bin/pip install coverage

bin/nosetests: bin/python
	bin/pip install nose

bin/coverage: bin/python
	bin/pip install coverage

bin/pylint: bin/python
	bin/pip install pylint

bin/flake8: bin/python
	bin/pip install flake8

bin/pyflakes: bin/python
	bin/pip install pyflakes

bin/pep8: bin/python
	bin/pip install pep8

bin/mkrelease: bin/python
	bin/pip install jarn.mkrelease
