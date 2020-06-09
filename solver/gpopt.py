import GPy
import GPyOpt
import numpy as np

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
        bounds.append({'name': f'x{i}', 
                       'type': 'continuous', 
                       'domain': (lower_bounds[i],upper_bounds[i])})
    f = lambda x: objective(x.ravel())
    BO_GP = GPyOpt.methods.BayesianOptimization(f=f,
                                                domain=bounds,
                                                initial_design_numdata=5,
                                                acquisition_type='LCB')
    BO_GP.run_optimization(max_iter=max_evals) #max_evalsじゃないかも
    x_best = BO_GP.x_opt
    y_best = BO_GP.fx_opt
    x_list = BO_GP.X
    y_list = BO_GP.Y