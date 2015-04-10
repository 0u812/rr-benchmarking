# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:36:06 2015

@author: phantom
"""
import antimony

ant = '''
model stoch()
  species A,B,C,D,E
  A -> B; k1
  B -> C; k2
  C -> D; k3
  D -> C; k4
  E -> C; k5
  
  A = 100000
  B = 1000
  C = 1000
  D = 1000
  E = 100000
  
  k1 = 0.2
  k2 = 0.05
  k3 = 0.1
  k4 = 0.01
  k5 = 0.05
end
'''

antimony.loadAntimonyString(ant)
sbmlstr = antimony.getSBMLString(antimony.getMainModuleName())
#print(sbmlstr)
with open('stoch_l3.xml', 'w') as f:
    f.write(sbmlstr)
