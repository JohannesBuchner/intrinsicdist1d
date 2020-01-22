import numpy as np

def generate_data(N, frac_outliers, frac_uplims, mean, width):
	is_outlier = np.random.uniform(size=N) < frac_outliers
	is_uplim = np.random.uniform(size=N) < frac_uplims
	means = np.where(is_outlier, np.random.uniform(0, 100, size=N),
		np.random.normal(mean, width, size=N))
	uncertainties = np.random.uniform(1, 3, size=N) * np.random.uniform(1, 3, size=N) * np.random.uniform(1, 3, size=N)
	M = 1000
	filename = 'N%d_out%.2f_ul%.2f_mean%.2f_pm%.2f.txt.gz' % (N, frac_outliers, frac_uplims, mean, width)
	posterior_samples = np.random.normal(means.reshape((1, -1)), uncertainties.reshape((1, -1)), size=(M, N))
	posterior_samples = np.where(is_uplim.reshape((1, -1)), np.random.uniform(0, means + uncertainties, size=(M, N)), posterior_samples)
	print(posterior_samples.shape)
	np.savetxt(filename, posterior_samples)


frac_uplims = 0.0
N = 100

for frac_outliers in 0., 0.02, 0.1:
	for mean in 0., 30., 60., 90.0:
		for width in 10., 50.0:
			generate_data(N, frac_outliers=frac_outliers, frac_uplims=frac_uplims, 
				mean=mean, width=width)

