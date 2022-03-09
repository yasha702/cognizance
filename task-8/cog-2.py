import numpy as np
#Question-2
A = np.random.randint(2,9,6)
B = np.random.randint(1,10,6)
equal = np.allclose(A,B)
print(A)
print(B)
print(equal)