import numpy as np

data = np.array([11, 22, 33, 44, 55])
data02 = np.array([[11, 22, 33, 44, 55],
                  [11, 22, 33, 44, 55]])
method = input()

if method == 'col':
    data = data.reshape((1, data.shape[0]))
elif method == 'row':
    data = data.reshape((data.shape[0], 1))

print(data)
print(data02)
dataT =data02.T
print(dataT)