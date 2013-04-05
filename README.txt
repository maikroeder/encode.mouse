.. contents::

Introduction
============

The ENCODE RNA Dashboard (mm9) provides a summary of transcriptome data 
production within the ENCODE project.

    http://genome.crg.es/encode_RNA_dashboard/mm9/
 
Installation
============

In order to install the dependencies, and put the necessary scripts into the
bin folder, run:

    make build

Template Preview
================

The templates that make up the dashboard can be rendered individually:

    source dashboard.txt

The templates are rendered individually, and can be previewed.

Dashboard Generation
====================

The templates can be rendered together to produce the complete dashboard:

    ./bin/pigeonhole dashboard.txt -v -c encode/mouse/page/page.ini -O encode/mouse/apache_export encode/mouse/page/input

Using the Pigeonhole tool, the mr.bob commands are run once to catch their
configuration, and then reused as many times as needed to produce the final
dashboard.

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
