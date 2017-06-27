import numpy as np

# Remember to import numpy before trying to use it ^^^

# Numpy Arrays
a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1, 2, 3], [4, 5, 6]])    # Create a rank 2 array
print(b.shape)    # Prints "(2, 3)"
print(b)
print(b[0, 0], b[0, 1], b[1, 0])

# Numpy given functions for building arrays, others available at:
# https://docs.scipy.org/doc/numpy/user/basics.creation.html#arrays-creation
a = np.zeros((2, 2))  # create an array of all 0.0's
print(a)
b = np.ones((1, 2))  # create an array of all 1.0's
print(b)
c = np.full((2, 2), 7)  # create an array filled with a constant value
print(c)
d = np.eye(2)  # create the identity matrix of the given size
print(d)
e = np.random.random((2, 2))  # Create an array filled with random values between 0 & 1
print(e)

#  Numpy slicing:
print("Numpy slicing")
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# Use slicing to REFERENCE the subarray consisting of the first 2 rows and columns 1 and 2
b = a[:2, 1:3]
print(b)
# A slice of an array is a view into the same data, so modifying it will modify the original array.
print(a[0, 1])
b[0, 0] = 77
print(a)
print(b)
a[1, 2] = -15
print(a)
print(b)


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
print(a)
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)


a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"

# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]])  # Prints "[2 2]"

# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"
# Create a new array from which we will select elements


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)  # prints "array([[ 1,  2,  3],
          #                [ 4,  5,  6],
          #                [ 7,  8,  9],
          #                [10, 11, 12]])"

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10
print(a)


a = np.array([[1, 2], [3, 4], [5, 6]])
bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                    # this returns a numpy array of Booleans of the same
                    # shape as a, where each slot of bool_idx tells
                    # whether that element of a is > 2.

print(bool_idx)

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print(a[a > 2])     # Prints "[3 4 5 6]"


# NumPy data types, docs here : https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html
x = np.array([1, 2])   # Let numpy choose the datatype
print(x.dtype)         # Prints "int64"

x = np.array([1.0, 2.0])   # Let numpy choose the datatype
print(x.dtype)             # Prints "float64"

x = np.array([1, 2], dtype=np.int32)   # Force a particular datatype
print(x.dtype)


# Array Maths
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Element wise sum
print(x + y)
print(np.add(x, y))

# Element wise difference
print(x - y)
print(np.subtract(x, y))

# Element wise product
print(x * y)
print(np.multiply(x, y))

# Element wise division
print(x / y)
print(np.divide(x, y))

# Element wise square root
print(np.sqrt(x))

# Matrix Maths
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

# Inner product of vectors
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce a rank 1 array
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce a rank 2 array
print(x.dot(y))
print(np.dot(x, y))

# More Maths functions, full list in Docs: https://docs.scipy.org/doc/numpy/reference/routines.math.html

x = np.array([[1, 2], [3, 4]])

print(np.sum(x))  # Compute sum of all elements
print(np.sum(x, axis=0))  # Compute sum of each column
print(np.sum(x, axis=1))  # Compute sum of each row

x = np.array([[1, 2], [3, 4]])
print(x)
print(x.T)

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1, 2, 3])
print(v)
print(v.T)


# Broadcasting
# We will add the vector v to each row of the matrix x, storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))   # Stack 4 copies of v on top of each other
print(vv)                 # Prints "[[1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]]"
y = x + vv  # Add x and vv elementwise
print(y)  # Prints "[[ 2  2  4
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)  # Prints "[[ 2  2  4]
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"

# Broadcasting two arrays together follows these rules:

# If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.
# The two arrays are said to be compatible in a dimension if they have the same size in the dimension, or if one of the arrays has size 1 in that dimension.
# The arrays can be broadcast together if they are compatible in all dimensions.
# After broadcasting, each array behaves as if it had shape equal to the elementwise maximum of shapes of the two input arrays.
# In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension
