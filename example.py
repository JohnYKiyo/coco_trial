import GPy
import GPyOpt
import numpy as np 

def objective(x):
    return np.cos(1.5*x) + 0.1*x

budget = 100

bounds = [{'name': 'x', 'type': 'continuous', 'domain': (0,10)}]
BO_GP = GPyOpt.methods.BayesianOptimization(f=objective, 
                                            domain=bounds,
                                            initial_design_numdata=5,
                                            acquisition_type='LCB')
BO_GP.run_optimization(max_iter=budget)
print("min:\t", BO_GP.fx_opt)
print("argmin:\t", BO_GP.x_opt)