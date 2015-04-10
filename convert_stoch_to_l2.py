from __future__ import print_function

import libsbml
from libsbml import SBMLReader, SBMLDocument, writeSBML

import os
from os import listdir
import sys
from sys import exit

dirs = ['stoch']
 
for d in dirs:
  for modelfile in filter(lambda x: '.xml' in x, listdir(d)):
    if not 'l3' in modelfile:
      print('skipping {}'.format(modelfile))
      continue

    print('converting {}'.format(modelfile))

    reader = SBMLReader()

    document = reader.readSBML(os.path.join(d,modelfile))

    errors = document.getNumErrors();

    if (errors > 0):
      print("Encountered the following SBML errors:" + "\n");
      document.printErrors();
      print("Conversion skipped.  Please correct the problems above first."
      + "\n");
      break

    #
    # If the given model is not already L2v4, assume that the user wants to
    # convert it to the latest release of SBML (which is L2v4 currently).
    # If the model is already L2v4, assume that the user wants to attempt to
    # convert it down to Level 1 (specifically L1v2).
    #

    olevel = document.getLevel();
    oversion = document.getVersion();
    success = False;
    outputFile = os.path.join(d, modelfile.replace('l3', 'l2v4'))

    print ("Attempting to convert Level " + str(olevel) + " Version " + str(oversion)
                                + " model to Level 2 Version 4." + "\n", file=sys.stderr);
    success = document.setLevelAndVersion(2, 4);

    errors = document.getNumErrors();

    if (not success):
      print("Unable to perform conversion due to the following:" + "\n", file=sys.stderr);
      document.printErrors();
      print("\n", file=sys.stderr);
      print("Conversion skipped.  Either libSBML does not (yet)" + "\n"
                                + "have the ability to convert this model or (automatic)" + "\n"
                                + "conversion is not possible in this case." + "\n", file=sys.stderr);

      break
    elif (errors > 0):
      print("Information may have been lost in conversion; but a valid model ", file=sys.stderr);
      print("was produced by the conversion.\nThe following information ", file=sys.stderr);
      print("was provided:\n", file=sys.stderr);
      document.printErrors();
      writeSBML(document, outputFile);
    else:
      print("Conversion completed." + "\n", file=sys.stderr);
      writeSBML(document, outputFile);