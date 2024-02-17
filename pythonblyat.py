import numpy as np

array_3d = np.random.random((10, 10, 3))
array_1d = array_3d.flatten()
print(array_3d.shape)
print(array_1d)