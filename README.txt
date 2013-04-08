.. contents::

Introduction
============

The ENCODE RNA Dashboard (mm9) provides a summary of transcriptome data 
production within the ENCODE project.

    http://genome.crg.es/encode_RNA_dashboard/mm9/

You can reproduce this dashboard with the encode.mouse Python package.
 
Installation
============

In order to install the dependencies, run:

    make build

This will install the right Python packages and put the necessary 
scripts into the bin folder.

Dashboard Generation
====================

The ENCODE Mouse dashboard data is read from the following location:

    encode/mouse/apache_export/mm9_RNA_dashboard_files.txt

The following command renders the ENCODE Mouse dashboard with Pigeonhole:

    ./bin/pigeonhole dashboard.txt -v -c encode/mouse/page/page.ini -O encode/mouse/apache_export encode/mouse/page/input

You can then open the resulting dashboard:

    encode/mouse/apache_export/index.html

Implementation
==============

Pigeonhole extends Bob, a flexible tool specially designed for rendering 
directory structure templates.

In an initial phase, Pigeonhole reads the dashboard.txt file that contains the 
exact command line calls for rendering the templates with Bob, and runs 
all of them internally for reusing them later.

The command line contains a number of options after "dashboard.txt":

    -v -c encode/mouse/page/page.ini -O encode/mouse/apache_export encode/mouse/page/input

Pigeonhole internally calls Bob with these parameters, only this time the 
the top level template contained in 

    encode/mouse/page

renders lower level templates recursively through callback slots embedded 
in the templates, that were ignored in the initial phase.

The callbacks pass on an ever reduced data set of the ENCODE Mouse dashboard to the
lower level templates until the templates from the lowest level have been rendered.

Template Preview
================

The templates that make up the dashboard can be rendered in batch mode:

    source dashboard.txt

You can now preview all the rendered templates:

    open encode/mouse/*/output/*.html

You can also rendered them individually like this, if you want to change the Bob parameters:

    ./bin/mrbob -v -c encode/mouse/header/header.ini -O encode/mouse/header/output encode/mouse/header/input

In this example, the result can be previewed in a browser by opening

    open encode/mouse/header/output/header.html

The templates here use the whole data from the ENCODE Mouse dashboard, which
makes them bulky, but it does have two great advantages:

1. It is rather practical to get a good overview of how the rendering will
look for all the different types of data. 

2. Rendering all data will also make sure that the template does not break,
for example when there is missing data.

Dependencies
============

The ENCODE RNA Dashboard (mm9) is produced with the help of the following 
Open Source Python packages:

- For rendering, the zope.pagetemplate module is used:
  https://pypi.python.org/pypi/zope.pagetemplate

- Pandas provides the data structures:
  https://pypi.python.org/pypi/pandas

- mr.bob is used to render the templates individually:
  https://pypi.python.org/pypi/mr.bob

- Pigeonhole is used for assembling the dashboard from the templates:
  https://pypi.python.org/pypi/pigeonhole
