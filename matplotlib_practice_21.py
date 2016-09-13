import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# JB's favorite Seaborn settings for notebooks
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load in data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Make bin boundaries
bins = np.arange(1700, 2501, 50)

# _ = plt.hist(xa_low, bins=bins)

# Add axis labels
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count')


# Reset bins, since xa_low has smaller values
bins = np.arange(1600, 2501, 50)

# Generate the histogram for the low-density fed mother
_ = plt.hist((xa_low, xa_high), bins=bins)

# Add axis labels
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count')

# Add a legend
plt.legend(('low', 'high'), loc='upper right')

plt.show()
