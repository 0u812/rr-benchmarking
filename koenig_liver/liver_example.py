# -*- coding: utf-8 -*-
'''
#########################################################################    
# Galactose Challenge / Clearance
#########################################################################  
Steady state clearance of galactose under given galactose challenge.
Here the clearance parameters and the GEC can be calculated from the model.

@author: Matthias Koenig
@date: 2015-02-12
'''

import numpy as np
import roadrunner_tools as rt

#########################################################################    
# Load model
#########################################################################    
# galactose challenge under constant flow
sbml_file = 'Galactose_v107_Nc20_galchallenge.xml'
r = rt.load_model(sbml_file)

#########################################################################    
# Set selection
#########################################################################    
compounds = ['alb', 'gal', 'galM', 'h2oM', 'rbcM', 'suc']
sel = ['time']
sel += ['[{}]'.format(item) for item in r.model.getBoundarySpeciesIds()]
sel += ['[PV__{}]'.format(item) for item in compounds]
sel += ['[PP__{}]'.format(item) for item in compounds]
sel += ['[{}]'.format(item)for item in r.model.getFloatingSpeciesIds() if item.startswith('H')]
sel += ['[{}]'.format(item)for item in r.model.getFloatingSpeciesIds() if item.startswith('D')]
sel += [item for item in r.model.getReactionIds() if item.startswith('H')]
sel += [item for item in r.model.getReactionIds() if item.startswith('D')]
sel += ["peak"]
r.selections = sel

#########################################################################    
# Set parameters & simulate
######################################################################### 
# galactose challenge periportal
gal_challenge = np.arange(start=0, stop=9.0, step=1.0) # [mM]

# initial concentration changes for simulation
inits = {}
# parameter dictionaries for the simulation
parameter_list = []
for gal in gal_challenge:
    parameter_list.append( {'gal_challenge': gal} )

# perform the simulations
# handled via helper function to achieve proper update of parameters, concentrations,
# depending rates and initial concentrations
ode_results = [rt.simulation(r, p, inits, absTol=1E-4, relTol=1E-4) for p in parameter_list]

#########################################################################    
# Figures
######################################################################### 
# PP - PV gal difference
# Plot the periportal to perivenious changes in galactose concentrations
# dynamical clearance effect
import pylab as p
for res in ode_results:
    s, gp = res
    p.plot(s['time'], s['[PP__gal]'], '-b')    
    p.plot(s['time'], s['[PV__gal]'], '-k')    
p.xlim([0, 10000])
p.title('PP and PV galactose')
p.xlabel('time [s]')
p.ylabel('galactose [mM]')
p.show()


