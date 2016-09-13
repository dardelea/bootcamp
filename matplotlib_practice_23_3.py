import numpy as np
import scipy.special

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)


# Part 1
def ecdf(data):
    '''Computes EDCF from data'''
    x = np.sort(data)
    y = (np.arange(0, len(x)) + 1) / len(x)
    return (x, y)

# Part 2
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Part 3
xa_high_x, xa_high_y = ecdf(xa_high)
xa_low_x, xa_low_y = ecdf(xa_low)

# Part 4
plt.plot(xa_high_x, xa_high_y, marker='.', linestyle='none')
plt.plot(xa_low_x, xa_low_y, marker='.', linestyle='none')

# Part 5
# Add axis labels
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('ECDF')
plt.margins(0.02)
# Add a legend
plt.legend(('low', 'high'), loc='lower right')

plt.show()
