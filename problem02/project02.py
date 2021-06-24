import numpy as np
from numpy import linalg

def fibo_num(index):
    if (index == 0) or (index == 1):
        return 1
    else:
        return fibo_num(index-1) + fibo_num(index-2)

def linalg_fibo(index):
    S = np.array([[.5+np.math.sqrt(5)/2,.5-np.math.sqrt(5)/2], [1,1]])
    A = np.array([[.5+np.math.sqrt(5)/2,0], [0,.5-np.math.sqrt(5)/2]])
    A_k = np.linalg.matrix_power(A,index)
    c = np.array([(5+np.math.sqrt(5))/10,(5-np.math.sqrt(5))/10])
    return np.matmul(np.matmul(S,A_k),c)[0]

for i in range(10):
    print(linalg_fibo(i))



