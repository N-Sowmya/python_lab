import numpy as np

mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
middle_row = mat[1]
print("Middle row:", middle_row)
column_sums = mat.sum(axis=0)
print("Column sums:", column_sums)


