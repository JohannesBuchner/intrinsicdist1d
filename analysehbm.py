import numpy as np
import sys
import matplotlib.pyplot as plt
from numpy import pi, log, exp

filename = sys.argv[1]
data = np.loadtxt(filename)
prefix = filename.replace('.txt', '').replace('.gz', '')

M, N = data.shape
assert N == 100

# hierarchical bayesian model
params = ['mean', 'std', 'frac_outliers']
def prior_transform(cube):
	params = cube.copy()
	params[0] = cube[0] * 100 # mean
	params[1] = 10**(cube[1] * 2) # std
	params[2] = 10**(-2 * cube[2] - 1) # frac_outliers
	return params

def loglikelihood(params):
	mean, std, frac_outliers = params
	prob = exp(-0.5 * ((data - mean)/std)**2 - log(2 * pi * std))
	assert prob.mean(axis=0).shape == (N,)
	return log(1e-100 + prob.mean(axis=0)).sum() # * (1 - frac_outliers) + frac_outliers + 1e-100).sum()

from ultranest import ReactiveNestedSampler

sampler = ReactiveNestedSampler(params, loglikelihood, transform=prior_transform,
	log_dir=prefix + '_gauss_outliers', resume='overwrite')
sampler.run()
sampler.plot()






