#!/usr/bin/env python
import sys
import argparse
from s23proj import Works

parser = argparse.ArgumentParser()

parser.add_argument("-rt", "--reftype", help="The type of reference you which to output. Options are 'bibtex' and 'ris'")
parser.add_argument("doi", help="The DOI of the paper")

args = parser.parse_args()
doi = args.doi
work = Works(doi)

if args.reftype == "bibtex":
    print(work.bibtex)
elif args.reftype == "ris":
    print(work.ris)
else:
    raise RuntimeError("Support for the citation style which you requested does not exist.")
