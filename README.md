# OSINT-Enrichment

This repository contains all the material from the talk "OSINT and my quest for Grouping" given at Bsides 

ct.py.pdf - Extract sub-domains for a given domain using crt.sh RSS feed
censys.py - Extract sub-domains for a given domain using Censys.io API
doing_recon_like_its_2017.pdf - Slides from the talk


A common use case in investigative reporting is to research a given set of companies
or people by searching for their ownership, control and other relationships in
online databases. ``corpint`` augments that process by automating look-ups in
web services and building a network graph out of the resulting set of links. It
also provides an explicit way to accept and reject results from online research,
thus making sure the entire resulting graph is fact-checked.

## Installation

To run ``corpint`` you will want to have Python and PostgreSQL installed. You
may also want to install Neo4J if you intend to use the graph exporter feature.

It's recommended to run ``corpint`` inside a Python virtual environment. When you
have a [virtualenv](https://python-guide.readthedocs.io/en/latest/dev/virtualenvs/)
set up, clone the git repository and install the package:

```bash
$ git clone https://github.com/YoshaNir/OSINT-Enrichment.git
$ cd OSINT-Enrichment
$ python IPsEnrichment.py 
```

## Usage

Most of the usage of ``OSINT-Enrichment`` is handled via a command-line utility, which
allows users to enrich data from external sources, find duplicates proposed for
merging and generate output formats such as a Neo4J graph.

### Configuration

Some configuration is required to make  connect to the correct
database and to the right subset of the data in there.



### Enriching data from external sources

To run all the loaded entities against an online source, such as OpenCorporates,
and store the resulting matches, run the following command:

```bash
$ corpint enrich -o mysource opencorporates
```

Valid enrichers currently include ``opencorporates``, ``aleph``,
``alephdocuments``, ``gmaps``, and ``bvdorbis``. Some of these enrichers may
work better if API keys are provided:

* ``OPENCORPORATES_APIKEY`` a valid API key from OpenCorporates.
* ``GMAPS_APIKEY`` a Google Maps API key
* ``ALEPH_APIKEY``, ``ALEPH_HOST`` to specify an Aleph instance other than
  ``data.occrp.org``.
