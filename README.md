## Benchmarking procedure (JKM)

## Scripts

* `bench.py`: Performs ODE benchmarking for RoadRunner
* `jarnac_bench.jan`: Performs ODE benchmarking for Jarnac
* `model_stats.py`: Gathers number of species/reactions for each model
* `convert_sbml_to_l2.py`: Converts ODE benchmark models to SBML level 2
* `convert_stoch_to_l2.py`: Converts stochastic benchmark model to SBML level 2
* `jean_marie.py`: Runs just the Jean-Marie model in RoadRunner
* `testjar.py`: Andy's original Jarnac benchmark, relies on CPU usage polling

## Benchmarking Procedure

The bench.py script is a modified version of Andy's code
(changes include additional models and csv output),
and should be run as follows:
```
python ./bench.py >../results.csv
```

As both RoadRunner and Jarnac use species amounts (as opposed to concentrations) internally, *ALL* models were run with the same tolerance parameters, which
are set in bench.py:
```
absolute: 1.000000e-007
relative: 0.0001
```

In both roadrunner and Jarnac tests, the number of steps was set
to 50.

The Jarnac benchmarking script is jarnac_bench.jan, and is run in the Jarnac UI.

## Notes

*The jean_marie, biomod22, and biomod09 models caused errors in Jarnac and were excluded from benchmarking.
*The biomod09 model also resulted in errors in roadrunner.
*Memory exhaustion prevented Jarnac from completing three trials of the 450/500 Brusselator models. These were completed on a separate run of just the 450/500 Brusselator models.
* The timer resolution in Jarnac is milliseconds
