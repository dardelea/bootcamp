import numpy as np
import scipy.special

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# load data
data = np.loadtxt('data/collins_switch.csv', skiprows=2, delimiter=',')
iptg = data[:,0]
gfp = data[:,1]
sem = data[:,2]

_ = plt.errorbar(iptg, gfp, yerr=sem,  marker='.', linestyle='none')
plt.ylabel('GFP intensity')
plt.xlabel('IPTG concentration')
plt.ylim(-0.02, 1.02)
plt.xlim(8e-4, 15)
# Set log scale
plt.xscale('log')
plt.show()
