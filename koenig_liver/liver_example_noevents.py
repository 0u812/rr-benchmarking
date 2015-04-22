# -*- coding: utf-8 -*-

import roadrunner as rr
import csv
import time
from sys import stdout

csvwriter = csv.writer(stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

csvwriter.writerow([rr.getVersionStr()])
csvwriter.writerow(['Name', 'Run_time'])

print('Load Model ...')
r = rr.RoadRunner(r'Galactose_v107_Nc20_galchallenge_noevents.xml')
r.selections = r.selections + ["[PP__gal]", '[PV__gal]']


name = 'Koenig_Liver'
for n in range(3):
    # reset the model ! for repeated simulation
    r.reset()
    
    # perform integration
    absTol = 1E-8
    relTol = 1E-8
    absTol = absTol * min(r.model.getCompartmentVolumes()) # absTol relative to the amounts
    tend = 100
    tsteps = 1000
    
    start = time.clock()    
    startTime = time.time()
    m = r.simulate(0, tend, tsteps, absolute=absTol, relative=relTol, stiff=True, plot=False)
    # stiff solver necessary (unstiff not possible)    
    # m = r.simulate(0, tend, tsteps, absolute=absTol, relative=relTol, stiff=False, plot=False)
    
    endTime = time.time()
    csvwriter.writerow([name, endTime-startTime])

# set True for figure
if False:
    import pylab as p
    p.plot(m['time'], m['[PP__gal]'], '-b')    
    p.plot(m['time'], m['[PV__gal]'], '-k')    
    p.xlim([0, tend])
    p.ylim([0,8])
    p.title('PP and PV galactose')
    p.xlabel('time [s]')
    p.ylabel('galactose [mM]')
    p.show()
