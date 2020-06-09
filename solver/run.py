import argparse
from experiment import Experiment
import scipy_fmin
import gpopt
import skopt_lcb

parser = argparse.ArgumentParser()
parser.add_argument('--number-of-batches', type=int, default=1)
parser.add_argument('--current-batch', type=int, default=1)
parser.add_argument('--budget', type=int, default=1e2)
parser.add_argument('--suite-name', default='bbob')
args = parser.parse_args()

#exp = Experiment(suite_name=args.suite_name, solver=scipy_fmin.solve, algorithm_name='scp_fmin')
#exp = Experiment(suite_name=args.suite_name, solver=gpopt.solve, algorithm_name='gpy_lcb')
exp = Experiment(suite_name=args.suite_name, solver=skopt_lcb.solve, algorithm_name='skopt_lcb')
exp.run(budget=args.budget, current_batch=args.current_batch, number_of_batches=args.number_of_batches)