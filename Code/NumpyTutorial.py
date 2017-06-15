import numpy as np

# Remember to import numpy before trying to use it ^^^

# Numpy Arrays
a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1, 2, 3],[4, 5, 6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])

# Numpy given functions for building arrays, others available at:
# https://docs.scipy.org/doc/numpy/user/basics.creation.html#arrays-creation
a = np.zeros((2, 2))  # create an array of all 0's
print(a)
b = np.ones((1, 2))  # create an array of all 1's
print(b)
c = np.full((2, 2), 7)  # create an array filled with a constant value
print(c)
d = np.eye(2)  # create the identity matrix of the given size
print(d)
e = np.random.random((2, 2))  # Create an array filled with random values between 0 & 1
print(e)

# Numpy slicing:
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# Use slicing to pull out the subarray consisting of the first 2 rows and columns 1 and 2
b = a[:2, 1:3]
print(b)
# A slice of an array is a view into the same data, so modifying it will modify the original array.
print(a[0, 1])
b[0, 0] = 77
print(a[0, 1])
print(a, b)
