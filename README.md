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

I then tested these three functions with a few minimization algorithms implemented in [SciPy](https://docs.scipy.org/) using 100 random values ranging from -100 to 100:

| Opt. Method  | Function (y) | Percentage of correct results | Iterations |
|--------------|--------------|-------------------------------|------------|
| Powell       | 1            | 100                           | 3          |
| Powell       | 2            | 100                           | 3          |
| Powell       | 3            | 100                           | 3          |
| CG           | 1            | 79                            | 15         |
| CG           | 2            | 100                           | 20         |
| CG           | 3            | 100                           | 3          |
| BFGS         | 1            | 99                            | 313        |
| BFGS         | 2            | 100                           | 29         |
| BFGS         | 3            | 100                           | 6          |
| L-BFGS-B     | 1            | 97                            | 21         |
| L-BFGS-B     | 2            | 100                           | 21         |
| L-BFGS-B     | 3            | 79                            | 3          |
| TNC          | 2            | 39                            | 78         |
| TNC          | 3            | 99                            | 58         |
| SLSQP        | 2            | 100                           | 28         |
| SLSQP        | 3            | 100                           | 5          |
| trust-constr | 1            | 99                            | 54         |
| trust-constr | 2            | 100                           | 69         |
| trust-constr | 3            | 98                            | 8          |

Some of the algorithms used:
- [Powell](https://en.wikipedia.org/wiki/Powell%27s_method)
- [CG](https://en.wikipedia.org/wiki/Conjugate_gradient_method)
- [BFGS](https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm)
- [TNC](https://en.wikipedia.org/wiki/Truncated_Newton_method)