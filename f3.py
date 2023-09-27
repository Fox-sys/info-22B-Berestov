import numpy as np

matrix = np.array([
    [1, 2, 3, -4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, -3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, -2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, -6, 7],
    [1, 2, 3, 4, -5, 6, 7],
])

matrix = matrix.reshape(7*7,)

sm = 0
for i in range(1, len(matrix), 2):
    if matrix[i] > 0:
        continue

    sm += abs(matrix[i])
print(sm)
