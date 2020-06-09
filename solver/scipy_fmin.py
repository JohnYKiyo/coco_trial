import numpy as np
from numpy.random import rand
from scipy.optimize import fmin
#y_best = float('inf')
x_best = np.zeros(0)
x_list = []
#y_list = []

def solve(objective, 
          x0, 
          lower_bounds,
          upper_bounds, 
          dim, 
          eval_constraints, 
          max_evals):
    global x_best,x_list
    #y_best = float('inf')
    x_best = np.zeros(0)
    x_best = fmin(objective, x0)
    while (not objective.final_target_hit and  # apply restarts, if so desired
           objective.evaluations < dim * max_evals):
        x_best = fmin(objective, 
                      lower_bounds + (rand(dim) + rand(dim))*(upper_bounds - lower_bounds) / 2)
