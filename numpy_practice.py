import numpy as np

# Practice 1
my_arr_1 = np.arange(0, 11, dtype=float)
my_arr_2 = np.linspace(0, 10, num=11, dtype=float)

# Practice 2

# Load in data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas
    to diameters with commensurate units.
    """

    # Compute diameter from area
    diameter = np.sqrt(4 * xa / np.pi)

    return diameter

# Practice 3
A = np.array([[6.7, 1.3, 0.6, 0.7],
              [0.1, 5.5, 0.4, 2.4],
              [1.1, 0.8, 4.5, 1.7],
              [0.0, 1.5, 3.4, 7.5]])

b = np.array([1.1, 2.3, 3.3, 3.9])

# Slicing
# 1
print(A[0])
# 2
print(A[:,0], A[:,2])
print(A[:,[1,3]])
# 3
print(A[A>2])
# 4
print(np.diag(A))

# np.linalg module
# 1
x = np.linalg.solve(A, b)
# 2
np.allclose(b,np.dot(A, x))
# 3
A_t = np.transpose(A)
# 4
A_i = np.linalg.inv(A)

# transfor 2D array to 1D array
# 1
B = np.ravel(A)
# concatenated all lists inside A into one lists
# 2
B = np.reshape(B, (4, 4))
