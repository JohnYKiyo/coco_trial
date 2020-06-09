import numpy as np
from skopt import Optimizer

y_best = float('inf')
x_best = np.zeros(0)
x_list = []
y_list = []

def solve(objective, 
          x0, 
          lower_bounds,
          upper_bounds, 
          dim, 
          eval_constraints, 
          max_evals):
    global x_best,x_list,y_best,y_list
    y_best = float('inf')
    x_best = np.zeros(0)
    bounds = []
    for i in range(dim):
        bounds.append((lower_bounds[i], upper_bounds[i]))
    opt = Optimizer(bounds,acq_func="LCB")

    for t in range(int(max_evals-eval_constraints)):
        suggested = opt.ask()
        y = objective(suggested)
        opt.tell(suggested, y)
        x_list.append(suggested)
        y_list.append(y)
        if y_best > y:
            y_best = y
            x_best = suggested