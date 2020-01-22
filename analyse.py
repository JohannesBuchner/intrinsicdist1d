import numpy as np
import sys
import matplotlib.pyplot as plt


filename = sys.argv[1]
data = np.loadtxt(filename)
prefix = filename.replace('.txt', '').replace('.gz', '')

# plot data
lo, hi = data.min(), data.max()
lo, hi = 0, 100
bins = np.linspace(lo, hi, 40)
means = np.mean(data, axis=0)

total = 0
for j, i in enumerate(np.argsort(means)):
	dist, _ = np.histogram(data[:,i], bins=bins)
	plt.plot((bins[:-1] + bins[1:]) / 2., dist / dist.max() + j*0.3, color='k')
	total = total + dist

plt.savefig(prefix + 'hists.pdf', bbox_inches='tight')
plt.close()

median_samples = []
for i in range(10000):
	j = np.random.randint(0, data.shape[0], size=data.shape[1])
	selection = np.asarray([data[ji, ki] for ki, ji in enumerate(j)])
	median_samples.append(np.median(selection))

mean, width = np.mean(median_samples), np.std(median_samples)
plt.vlines([mean - width, mean, mean + width], 0, 1, linestyles=[':', '-', ':'])

for j, i in enumerate(np.argsort(means)):
	plt.plot((bins[:-1] + bins[1:]) / 2., total / total.max(), color='r')

plt.savefig(prefix + 'stackedhists.pdf', bbox_inches='tight')
plt.close()


# hierarchical bayesian model




