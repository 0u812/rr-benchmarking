# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:47:12 2015

@author: phantom
"""

import roadrunner as rr
import tellurium as te

r = rr.RoadRunner(r'C:\Users\phantom\Documents\devel\src\rr-benchmarking\jean_marie\Jean_Marie_AMPA16_RobHow_v6.xml')

print(r.rv())

print te.sbmlToAntimony(r.getCurrentSBML())
m = r.simulate(0, 5000000, 10000)
r.plot()