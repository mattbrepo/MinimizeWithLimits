# MinimizeWithLimits
Minimize a function using distance limits

**Language: Python**

**Start: 2024**

## Why
I wanted to use minimization algorithms to find values that are within certain distance limits (_lower lim_: 1.7, _upper lim_: 2.3) to a reference value (_x0_: 1). I implemented a few functions to calculate the error between a value and the reference value.

Here is a chart where 3 functions are shown (y1, y2, y3):

![chart](/images/chart1.png)

where the red line marks the reference value (_x0_) and the orange lines mark the two possible valid ranges.

The following chart shows the same functions, but on the x-axis, the distance from the reference value is shown:

![chart](/images/chart2.png)

I then tested these three functions with a few minimization algorithms implemented in [SciPy](https://docs.scipy.org/) using 100 random values:

| Opt. Method  | Function | Percentage of correct results  | Iterations |
|--------------|----------|--------------------------------|------------|
| [Powell](https://en.wikipedia.org/wiki/Powell%27s_method)       | 1        | 100                        | 2          |
| Powell       | 2        | 100                            | 2          |
| Powell       | 3        | 100                            | 2          |
| CG           | 1        | 100                            | 4          |
| CG           | 2        | 100                            | 7          |
| CG           | 3        | 100                            | 1          |
| [BFGS](https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm)     | 1        | 100                            | 9          |
| BFGS         | 2        | 100                            | 7          |
| BFGS         | 3        | 81                             | 5          |
| L-BFGS-B     | 1        | 100                            | 5          |
| L-BFGS-B     | 2        | 100                            | 5          |
| L-BFGS-B     | 3        | 81                             | 3          |
| TNC          | 1        | 98                             | 25         |
| TNC          | 2        | 100                            | 19         |
| TNC          | 3        | 99                             | 20         |
| SLSQP        | 1        | 100                            | 7          |
| SLSQP        | 2        | 100                            | 9          |
| SLSQP        | 3        | 100                            | 4          |
| trust-constr | 1        | 95                             | 18         |
| trust-constr | 2        | 100                            | 8          |
