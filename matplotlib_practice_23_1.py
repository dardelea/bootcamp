import numpy as np
import scipy.special

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Practice 1
# 1
data = np.loadtxt('data/collins_switch.csv', skiprows=2, delimiter=',')
# 2
iptg = data[:,0]
# 3
gfp = data[:,1]
# 4
_ = plt.semilogx(iptg, gfp, marker='.', linestyle='none')
# plt.margins(0.02) # margins
plt.ylim(-0.02, 1.02)
plt.xlim(8e-4, 15)
# 5
plt.ylabel('GFP intensity')
plt.xlabel('IPTG concentration')

plt.show()
