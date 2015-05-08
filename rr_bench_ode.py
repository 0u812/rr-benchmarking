#!/usr/bin/env python

# Roadrunner benchmarking script, Apr 2015
# Authors: Andy Somogyi, J Kyle Medley
# Language: Python 2.7.9
# Usage: cd <this_dir> && python bench.py >rr-ode-results.csv

from __future__ import print_function
from roadrunner import *
import time
import csv
from sys import stderr, stdout

convert_tol = False

absolute_tol_default = 1.000000e-007
rel_tol_default = 0.0001

Config.setValue(Config.SIMULATEOPTIONS_ABSOLUTE, absolute_tol_default)
Config.setValue(Config.SIMULATEOPTIONS_RELATIVE, rel_tol_default)

tests = [ \
  ('jean_marie', "./jean_marie/Jean_Marie_AMPA16_RobHow_v6.xml"),
  ('jana_wolf', "./jana_wolf/Jana_WolfGlycolysis.xml"),
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

start = 0;
end = 50;
steps = 50;

csvwriter = csv.writer(stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

def timeit(name, path):
  print('Model: {}'.format(name), file=stderr)
  startTime = time.time()

  # Load the model
  r=RoadRunner(path)

  loadTime = time.time()
  m=r.simulate(start, end, steps)
  endTime = time.time()

  csvwriter.writerow([name, loadTime-startTime, endTime-loadTime, endTime-startTime])

print(getVersionStr(), file=stderr)
csvwriter.writerow([getVersionStr()])

for n in range(3):
  print('Trial {}'.format(n+1), file=stderr)
  csvwriter.writerow(['Trial {}'.format(n+1)])
  csvwriter.writerow(['Name', 'Load_time', 'Run_time', 'Total_time'])
  for t in tests:
      timeit(*t)

