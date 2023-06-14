import numpy as np
import matplotlib.pyplot as plt
from gauss import show_result

x = np.array([1,2,3,5])
y = np.array([9,8,6,3])

# Regressão linear por mínimos quadrados

# Montagem da matriz A  e b
A = np.concatenate((np.array([1]*len(x)).reshape(-1,1),x.reshape(-1,1)),axis=1)
b = y.reshape(-1,1)


Aa = A.T.dot(A)
b = A.T.dot(b)

print(Aa)
print(b)

# método de gauss criado
show_result(Aa,b)




