# Liver model benchmark

**Galactose_v107_Nc20_galchallenge.xml**

Kinetic model of hepatic sinusoidal unit consisting of sinusoid, space of Disse and 20 Hepatocytes. In the example simulations the periportal galactose concentrations are altered and the timecourses of periportal (PP, inflow) and perivenous (PV, outflow) galactose are plotted over time.

**liver_examle.py**

Python scripts for simulation and visualization of the liver model example.

**roadrunner_tools.py**

Helper scipts for simulations with roadrunner. Handles complex changes of parameters, initial concentrations and subsequent updates of the derived values. Tolerances are handled via amounts.

**liver_examle.png**

Figure of periportal (PP) and perivenious (PV) galactose timecourses under varying galactose challenges periportal.

**liver_benchmark.csv**

Typical single core simulation times (duration) if all cores are running roadrunner simulations. Architectures of the different machines vary. Duration includes the database writes and file writing which are in the order of ~2s. So simulation times are t_sim ~ duration-2s.
