
import numpy as np

# Create a 2D NumPy array (matrix)
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("2D Array:\n", arr)

# Shape and size
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Number of dimensions:", arr.ndim)

# Row-wise and Column-wise operations
print("Row-wise sum:", np.sum(arr, axis=1))
print("Column-wise sum:", np.sum(arr, axis=0))

# Maximum and minimum
print("Maximum element:", np.max(arr))
print("Minimum element:", np.min(arr))

# Mean
print("Mean of all elements:", np.mean(arr))

# Transpose
print("Transpose:\n", np.transpose(arr))

# Diagonal elements
print("Diagonal elements:", np.diagonal(arr))

# Sorting
print("Row-wise sorted array:\n", np.sort(arr))