import numpy as np
from numpy import linalg
import time

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
    return int(np.round(np.matmul(np.matmul(S,A_k),c)[1]))

def solve_problem2(fibo_func):
    sum = 0
    index = 0
    current_fibo = 0
    t0 = time.time()
    while True:
        current_fibo = fibo_func(index)
        if current_fibo > 4000000:
            break
        if current_fibo%2 != 0:
            sum += current_fibo
            was_summed = True
        else:
            was_summed = False
        index += 1
    t1 = time.time()
    print('function:{} sum:{}, elapsed time{} '.format(fibo_func, sum, t1-t0))

for fibo_func in [fibo_num,linalg_fibo]:
    solve_problem2(fibo_func)