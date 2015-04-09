## Benchmarking procedure (JKM)

### Roadrunner:

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
to 500.
