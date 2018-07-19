# OSINT-Enrichment

This repository contains all the material from the talk "OSINT and my quest for Grouping" given at Bsides 

1. IPsEnrichment.py - Extract IP location, ASN and owners into subgroups
2. DomainsEnrichment.py - Extract top-level-domains and domain length into subgroups
3. MaliciousIPs and MaliciousDomains - OSINT list from AlienVault and Abuce.ch from Feb-May 2018


A common use case in investigative reporting is to research a given set of companies
or people by searching for their ownership, control and other relationships in
online databases. ``OSINT-Enrichment`` augments that process by automating look-ups. It
also provides an explicit way to accept and reject results from online research,
thus making sure the entire noise and unreletaed information can be dropped.

## Installation

To run ``OSINT-Enrichment`` you will want to have Python and pandas library installed. You
may also want to install ``numpy and matplotlib`` if you intend to use the graph exporter feature.

It's recommended to run ``OSINT-Enrichment`` inside a Python virtual environment. When you
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
$ OSINT-Enrichment.py enrich -o mysource opencorporates
```

Valid enrichers currently include ``opencorporates``, ``aleph``,
``alephdocuments``, ``gmaps``, and ``bvdorbis``. Some of these enrichers may
work better if API keys are provided:

* ``OPENCORPORATES_APIKEY`` a valid API key from OpenCorporates.
* ``GMAPS_APIKEY`` a Google Maps API key
* ``ALEPH_APIKEY``, ``ALEPH_HOST`` to specify an Aleph instance other than
  ``data.occrp.org``.
