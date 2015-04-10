# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:36:06 2015

@author: phantom
"""
import antimony

ant = '''
model stoch()
  species A,B,C,D,E
  A -> B; A
  B -> C; B
  C -> D; C
  D -> E; D
  E -> A; E
  
  A = 100000
  B = 0
  C = 0
  D = 0
  E = 0
end
'''

antimony.loadAntimonyString(ant)
sbmlstr = antimony.getSBMLString(antimony.getMainModuleName())
#print(sbmlstr)
with open('stoch_l3.xml', 'w') as f:
    f.write(sbmlstr)
