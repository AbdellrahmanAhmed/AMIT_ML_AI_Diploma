import numpy as np


def stats(var, axis='col'):
    matrix = np.array(var)
    if axis[0].lower() == 'c':
        axis = 0
    else:
        axis = 1
    if len(matrix.shape) == 1:
        mean = np.mean(matrix)
        var = np.var(matrix)
        std = np.std(matrix)
    else:
        mean = np.mean(matrix, axis=axis)
        var = np.var(matrix, axis=axis)
        std = np.std(matrix, axis=axis)


    return mean, var, std


v = np.array([1, 2, 3, 4, 5, 6])
m = np.arange(9).reshape(3, 3)
