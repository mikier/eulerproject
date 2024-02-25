import numpy as np

def is_palindrome(i):
    s = str(round(i))
    return s == s[::-1]

if __name__ == "__main__":
    x = np.linspace(1, 1000, 1000)
    y = np.linspace(1, 1000, 1000)
    M = np.outer(x.T,y)

    vect_is_palindrome = np.vectorize(is_palindrome)
    print(np.max(M[vect_is_palindrome(M)]))

    