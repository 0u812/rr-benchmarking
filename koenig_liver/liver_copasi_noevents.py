# -*- coding: utf-8 -*-
'''
Run SBML simulation with copasi.

SBML Load time: 241.893377, 239.276337, 216.685368, 214.499586105
Simulation time: 514.35285902, 456.029584885

'''
import copasi_tools


import csv
from sys import stdout
csvwriter = csv.writer(stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow(["COPASI"])
csvwriter.writerow(['Name', 'Run_time'])
name = 'Koenig_Liver_copasi'

sbml_file = r'Galactose_v107_Nc20_galchallenge_noevents.xml'
# sbml_file = r'test.xml'

N_benchmark = 1
for n in range(N_benchmark):    
    # perform integration
    absTol = 1E-8
    relTol = 1E-8
    tstart = 0
    tend = 100
    tsteps = 1000
    
    res = copasi_tools.simulate(filename=sbml_file, t0=tstart, duration=(tend-tstart), steps=tsteps, 
                   absTol=absTol, relTol=relTol, write_report=True)
    startTime = res["startTime"]    
    endTime = res["endTime"]
    
    csvwriter.writerow([name, endTime-startTime])

# timeseries = res["timeseries"]