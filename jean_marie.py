# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:47:12 2015

@author: phantom
"""

import roadrunner as rr
#import tellurium as te
import csv
import time
from sys import stderr, stdout

csvwriter = csv.writer(stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

csvwriter.writerow([rr.getVersionStr()])
csvwriter.writerow(['Name', 'Run_time'])

r = rr.RoadRunner(r'.\jean_marie\Jean_Marie_AMPA16_RobHow_v6.xml')

#print(r.rv())

name = 'JeanMarie'
for n in range(3):
    #print te.sbmlToAntimony(r.getCurrentSBML())
    startTime = time.time()
    m = r.simulate(0, 5000000, 10000)
    #r.plot()
    endTime = time.time()
    csvwriter.writerow([name, endTime-startTime])
