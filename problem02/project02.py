import numpy as np

def fibo_num(index):
    if (index == 0) or (index == 1):
        return 1
    else:
        return fibo_num(index-1) + fibo_num(index-2)

for i in range(10):
    print(fibo_num(i))

