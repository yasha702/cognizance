import numpy as np
# creating numpy array of type float64
ex_array = np.array([[11.21, 19.21], [46.21, 18.21], [29.21, 21.21]])
print(ex_array)

print('After converting numpy float array to int array')
int_array = ex_array.astype(int)
print(int_array)