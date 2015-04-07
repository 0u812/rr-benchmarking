# How to run Jarnac benchmarks interactively

* Click on the load SBML icon (must be level 2 SBML)
* Observe model is converted to Jarnac script
* Add the following lines:
```
t1 = timer;
m = p.sim.eval (0, 50, 50);
println "Time = ", (timer - t1)/1000, " secs";
```
* Run the script; output will be simulation time
