import numpy as np
import scipy.special
# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)
import bootcamp_utils


# Import data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Part 1
xa_high_x, xa_high_y = bootcamp_utils.ecdf(xa_high)
xa_low_x, xa_low_y = bootcamp_utils.ecdf(xa_low)

# Part 2
plt.plot(xa_high_x, xa_high_y, marker='.', linestyle='none')
plt.plot(xa_low_x, xa_low_y, marker='.', linestyle='none')

# Part 3

# Make smooth x-values
x = np.linspace(1600, 2500, 400)

# Compute theoretical Normal distribution
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale=np.std(xa_high))

# Part 4
plt.plot(x, cdf_low, color='grey')
plt.plot(x, cdf_high, color='grey')

# Part 5
# Add axis labels
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('ECDF')
plt.margins(0.02)
# Add a legend
plt.legend(('low', 'high'), loc='lower right')

plt.show()
