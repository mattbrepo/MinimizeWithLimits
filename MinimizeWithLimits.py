# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

l_lim = 1.7
u_lim = 2.3
x0 = 1
err_mode = 0

def my_func(x, x0, lb, ub, mode):
  d = np.sqrt((x0 - x)**2)
  if d < lb:
    if mode == 0:
      return d
    elif mode == 1:
      return ((2 * lb**2) / (lb**2 + d**2) - 1)**2
    elif mode == 2:
      return lb - d
    elif mode == 3:
      return (lb - d)**2

  elif d > ub:
    if mode == 0:
      return d
    elif mode == 1:
      return (d**2 / ub**2 - 1)**2
    elif mode == 2:
      return d - ub 
    elif mode == 3:
      return (d - ub)**2
  
  return 0

def my_func_xs(xs, x0, lb, ub, mode):
  return [my_func(x, x0, lb, ub, mode) for x in xs]

def err_func(xs):
  global l_lim, u_lim, err_mode, x0
  res = 0
  for x in xs:
    res = res + my_func(x, x0, l_lim, u_lim, err_mode)
  return res

# %%
x_lim = [-3, 5]
y_lim = [-0.2, 5]

xl = np.random.uniform(x_lim[0], x0, 2000)
xu = np.random.uniform(x0, x_lim[1], 2000)
                    
yl0 = my_func_xs(xl, x0, l_lim, u_lim, 0)
yl1 = my_func_xs(xl, x0, l_lim, u_lim, 1)
yl2 = my_func_xs(xl, x0, l_lim, u_lim, 2)
yl3 = my_func_xs(xl, x0, l_lim, u_lim, 3)

yu0 = my_func_xs(xu, x0, l_lim, u_lim, 0)
yu1 = my_func_xs(xu, x0, l_lim, u_lim, 1)
yu2 = my_func_xs(xu, x0, l_lim, u_lim, 2)
yu3 = my_func_xs(xu, x0, l_lim, u_lim, 3)

dl = np.sqrt((x0 - xl)**2)
du = np.sqrt((x0 - xu)**2)

plt.figure(figsize=(8, 6))
plt.axvline(x=x0-l_lim, color='orange', linestyle='-', label='')
plt.axvline(x=x0-u_lim, color='orange', linestyle='-', label='')
plt.axvline(x=x0, color='red', linestyle='-', label='')
plt.axvline(x=x0+l_lim, color='orange', linestyle='-', label='')
plt.axvline(x=x0+u_lim, color='orange', linestyle='-', label='')

#plt.scatter(xl, yl0, color='cyan', s=1, label='y0')
#plt.scatter(xu, yu0, color='cyan', s=1, label='')
plt.scatter(xl, yl1, color='green', s=1, label='y1')
plt.scatter(xu, yu1, color='green', s=1, label='')
plt.scatter(xl, yl2, color='blue', s=1, label='y2')
plt.scatter(xu, yu2, color='blue', s=1, label='')
plt.scatter(xl, yl3, color='magenta', s=1, label='y3')
plt.scatter(xu, yu3, color='magenta', s=1, label='')

plt.title(f'X0: {x0}, optimal ranges: [{x0-u_lim:.1f}, {x0-l_lim:.1f}], [{x0+l_lim:.1f}, {x0+u_lim:.1f}]')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.legend()
plt.grid(True)
plt.show()

# %%
plt.figure(figsize=(8, 6))
plt.axvline(x=l_lim, color='orange', linestyle='-', label='')
plt.axvline(x=u_lim, color='orange', linestyle='-', label='')

#plt.scatter(dl, yl0, color='cyan', s=1, label='y0')
#plt.scatter(du, yu0, color='cyan', s=1, label='')
  
plt.scatter(dl, yl1, color='green', s=1, label='y1')
plt.scatter(du, yu1, color='green', s=1, label='')
plt.scatter(dl, yl2, color='blue', s=1, label='y2')
plt.scatter(du, yu2, color='blue', s=1, label='')
plt.scatter(dl, yl3, color='magenta', s=1, label='y3')
plt.scatter(du, yu3, color='magenta', s=1, label='')

plt.title(f'distance range [{l_lim}, {u_lim}]')
plt.xlabel('d')
plt.ylabel('y')
plt.xlim([0, 1.7*u_lim])
plt.ylim(y_lim)
plt.legend()
plt.grid(True)
plt.show()

# %%
x = np.random.uniform(x_lim[0], x_lim[1], 100)

scipy_methods = ['Nelder-Mead', 'Powell', 'CG', 'BFGS', 'L-BFGS-B', 'TNC', 'SLSQP', 'trust-constr']
for method in scipy_methods:
  for mode in [1,2,3]:
    err_mode = mode
    res_scipy = optimize.minimize(err_func, x, method=method)
    print(f'{method}, mode: {err_mode}, success: {res_scipy.success}, x: [{min(res_scipy.x):.2f}..{max(res_scipy.x):.2f}], in range: {((x0-u_lim <= res_scipy.x) & (res_scipy.x <= x0-l_lim) | (x0+l_lim <= res_scipy.x) & (res_scipy.x <= x0+u_lim)).sum()} on {len(res_scipy.x)}, iters: {res_scipy.nit}')
