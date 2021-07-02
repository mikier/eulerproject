import numpy as np
import matplotlib.pyplot as plt
import re

def is_palindrome(num):
    return str(num)==str(num)[::-1]

largest_palindrome = 0

for i in range(1,999):
    for j in range(1,999):
        num = i*j
        #print(i, j , num, is_palindrome(num))
        if is_palindrome(num) and num>largest_palindrome:
            largest_palindrome = (num)

print(largest_palindrome)

        


