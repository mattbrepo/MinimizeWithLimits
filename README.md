# MinimizeWithLimits
Minimize a function using distance limits

**Language: Python**

**Start: 2024**

## Why
I wanted to use minimization algorithms to find values that are within certain distance limits (_lower lim_: 1.7, _upper lim_: 2.3) to a reference value (_x0_: 1). I implemented a few functions to calculate the error between the value and the reference value.

Here is a chart where 3 functions are shown (y1, y2, y3):

![chart](/images/chart1.jpg)

where the red line marks the reference value (_x0_) and the orange lines mark the two possible valid ranges.

The following chart shows the same functions, but on the x-axis the distances of the values from the reference value are shown:

![chart](/images/chart2.jpg)

I then tested these three functions with a few minimization algorithms implemented in [SciPy](https://docs.scipy.org/) using 100 random values:

| Opt. Method  | Function | Result values | # of correct   | Iterations |
|--------------|----------|---------------|----------------|------------|
| Powell       | 1        | [-1.29..3.29] | 100            | 2          |
| Powell       | 2        | [-1.29..3.22] | 100            | 2          |
| Powell       | 3        | [-1.29..3.13] | 100            | 2          |
| CG           | 1        | [-1.30..3.30] | 100            | 4          |
| CG           | 2        | [-1.30..3.30] | 100            | 7          |
| CG           | 3        | [-1.30..3.30] | 100            | 1          |
| BFGS         | 1        | [-1.30..3.30] | 100            | 9          |
| BFGS         | 2        | [-1.29..3.30] | 100            | 7          |
| BFGS         | 3        | [-1.30..3.30] | 81             | 5          |
| L-BFGS-B     | 1        | [-1.30..3.30] | 100            | 5          |
| L-BFGS-B     | 2        | [-1.27..3.25] | 100            | 5          |
| L-BFGS-B     | 3        | [-1.30..3.30] | 81             | 3          |
| TNC          | 1        | [-1.29..3.30] | 98             | 25         |
| TNC          | 2        | [-1.29..3.27] | 100            | 19         |
| TNC          | 3        | [-1.30..3.30] | 99             | 20         |
| SLSQP        | 1        | [-1.30..3.30] | 100            | 7          |
| SLSQP        | 2        | [-1.28..3.21] | 100            | 9          |
| SLSQP        | 3        | [-1.30..3.30] | 100            | 4          |
| trust-constr | 1        | [-1.30..3.30] | 95             | 18         |
| trust-constr | 2        | [-1.24..3.27] | 100            | 8          |
| trust-constr | 3        | [-1.30..3.30] | 52             | 5          |








