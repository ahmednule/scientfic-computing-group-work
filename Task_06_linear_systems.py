import numpy as np


# 2x + 3y = 8 and 4x + y = 6
A = np.array([[2.0, 3.0], [4.0, 1.0]])
b = np.array([8.0, 6.0])
solution = np.linalg.solve(A, b)

print("Solution [x, y]:", solution)
print("Residual:", A @ solution - b)
