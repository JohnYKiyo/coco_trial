from cocoex import default_observers
from cocoex import Observer
from cocoex import Suite
from cocoex.utilities import ObserverOptions
from tqdm import tqdm
from typing import Callable  # NOQA
from typing import Optional  # NOQA
from scipy.optimize import fmin

class Experiment(object):
    def __init__(self,
                 solver,
                 suite_name="bbob",
                 suite_instance="",
                 suite_options="dimensions: 2,3",
                 algorithm_name=None):
        self._solver = solver
        self._suite_name = suite_name
        self._suite_instance = suite_instance
        self._suite_options = suite_options
        self._algorithm_name = algorithm_name
        
    def _build_observer_options(self, budget):
        # type: (int) -> ObserverOptions
        '''
        self._algorithm_name = 'hoge'
        self._suite_name = 'bbob'
        budget = 100
        return {'result_folder': '"hoge/on_bbob_budget0100xDim"', 'algorithm_name': 'hoge'}
        '''
        opts = {
            'result_folder':
            '"%s/on_%s_budget%04dxDim"' %
            (self._algorithm_name, self._suite_name, budget),
            'algorithm_name': self._algorithm_name
        }
        return ObserverOptions(opts) 

    def run(self,budget=1e1, # use 1e1 or even 2 for a quick first test run
            current_batch=1, 
            number_of_batches=15):
        suite = Suite(self._suite_name,self._suite_instance,self._suite_options) #bbox関数パッケージリストみたいなやつ
        observer_name = default_observers()[self._suite_name] 
        observer_options = self._build_observer_options(budget)
        observer = Observer(observer_name, observer_options.as_string)
        #observer = Observer("bbob", "result_folder: myoptimizer-on-bbob")
        
        for p_index, p in enumerate(tqdm(suite)):# loop over all problems
            if (p_index % number_of_batches) != current_batch - 1:
                continue
            observer.observe(p)# prepare logging of necessary data
            max_evals = budget * p.dimension
            self._solver(p,
                         p.initial_solution,
                         p.lower_bounds,
                         p.upper_bounds,
                         p.dimension,
                         p.evaluations_constraints,
                         max_evals)

#for p in suite:  # loop over all problems
#    observer.observe(p)  # prepare logging of necessary data
#    fmin(p, p.initial_solution)  # disp=False would silence fmin output
#    while (not p.final_target_hit and  # apply restarts, if so desired
#           p.evaluations < p.dimension * budget_multiplier):
#        fmin(p, p.lower_bounds + (rand(p.dimension) + rand(p.dimension)) *
#                    (p.upper_bounds - p.lower_bounds) / 2)
    