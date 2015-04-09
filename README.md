## Benchmarking procedure (JKM)


The bench.py script is a modified version of Andy's code
(changes include additional models and csv output),
and should be run as follows:
```
python ./bench.py >../results.csv
```

*ALL* models were run with the same tolerance parameters, which
are set in bench.py:
```
absolute: 1.000000e-007
relative: 0.0001
```

In both roadrunner and Jarnac tests, the number of steps was set
to 50.

The Jarnac benchmarking script is jarnac_bench.jan, and is run in the Jarnac UI.
The jean_marie, biomod22, and biomod09 models caused errors in Jarnac and were excluded from benchmarking.
The biomod09 model also resulted in errors in roadrunner.
Memory exhaustion prevented Jarnac from completing three trials of the 450/500 Brusselator models.
