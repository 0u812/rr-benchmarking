#!/usr/bin/env python

# Get number of species/reactions for each benchmark model      , Apr 2015
# Authors: J Kyle Medley
# Language: Python 2.7.9
# Usage: cd <this_dir> && python model_stats.py

from __future__ import print_function
import libsbml
from libsbml import SBMLReader, SBMLDocument, writeSBML
from sys import stderr, stdout
import os

tests = [ \
  ('jean_marie', "./jean_marie/Jean_Marie_AMPA16_RobHow_v6.xml"),
  ('jana_wolf', "./jana_wolf/Jana_WolfGlycolysis.xml"),
  # ('biomod09', "./biomod09/BIOMD0000000009.xml"), # crashes solver - JKM
  ('biomod14', "./biomod14/BIOMD0000000014.xml"),
  ('biomod22', "./biomod22/BIOMD0000000022.xml"),
  ('biomod33', "./biomod33/BIOMD0000000033.xml"),
  ('liver',    "./koenig_liver/Galactose_v107_Nc20_galchallenge_noevents.xml"),
  ('00001',   "./00001/00001-sbml-l2v4.xml"),
  ('00002',   "./00002/00002-sbml-l2v4.xml"),
  ('00050',  "./00050/00050-sbml-l2v4.xml"),
  ('00100', "./00100/00100-sbml-l2v4.xml"),
  ('00150', "./00150/00150-sbml-l2v4.xml"),
  ('00200', "./00200/00200-sbml-l2v4.xml"),
  ('00250', "./00250/00250-sbml-l2v4.xml"),
  ('00300', "./00300/00300-sbml-l2v4.xml"),
  ('00350', "./00350/00350-sbml-l2v4.xml"),
  ('00400', "./00400/00400-sbml-l2v4.xml"),
  ('00450', "./00450/00450-sbml-l2v4.xml"),
  ('00500', "./00500/00500-sbml-l2v4.xml")]

for t in tests:
  name = t[0]
  path = t[1]
  
  reader = SBMLReader()

  document = reader.readSBML(path)

  errors = document.getNumErrors();

  if (errors > 0):
    print("Encountered the following SBML errors:" + "\n", file=stderr);
    document.printErrors();
    print("Conversion skipped.  Please correct the problems above first."
      + "\n", file=stderr);
    continue
  
  model = document.getModel()
  
  print('{}: {} species and {} reactions'.format(name, model.getNumSpecies(), model.getNumReactions()))