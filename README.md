J Kyle Medley
## libRoadRunner/Jarnac Benchmarking

## Usage

You must have a deployment of libRoadRunner version 1.3.1 in your Python module 
search path before continuing. The benchmarking scripts can be run as follows:
```
git clone -b submission https://github.com/0u812/rr-benchmarking.git
cd rr-benchmarking
```

Run the roadrunner ODE benchmark and save the results to rr-ode-results.csv:
```
python ./bench.py >rr-ode-results.csv
```

Run the roadrunner stochastic benchmark and save the results to rr-ode-results.csv:
```
python ./bench.py >rr-stoch-results.csv
```
