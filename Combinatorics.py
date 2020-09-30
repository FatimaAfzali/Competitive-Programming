import math
from math import e, pi

def factorial(n):
    if n < 2: return 1
    i = 1
    for j in range(2, n+1):
        i *= j
    return i
    
def genComb(n, m = None): #matrix C s.t. C[a][b] = (a C b) mod m, with a, b \le n
    C = [[0 for i in range(n+1)] for j in range(n+1)]
    #C[i][j] = C[i-1][j] + C[i-1][j-1]
    for i in range(n+1):
        C[i][0] = 1
        C[i][1] = i
        C[i][i-1] = i
        C[i][i] = 1
    for i in range(2, n+1): 
        for j in range(2, i):
            if m == None:
                C[i][j] = (C[i-1][j] + C[i-1][j-1])
            else:
                C[i][j] = (C[i-1][j] + C[i-1][j-1])%m
    return C

def Fibonacci(n, m = None): 
    if n < 2: return n #F_0 = 0, F_1 = 1
    a, b = 0, 1
    for i in range(n-1):
        if m == None: 
            a, b = b, (a+b)
        else:
            a, b = b, (a+b)%m
    return b
#Binet's formula: F_n = (phi^n - (1-phi)^n)/sqrt(5)

def Catalan(n, C): #C is combination matrix
    return C[2*n][n] - C[2*n][n+1] #may be negative if mods have been used
    
def Derangement(n): 
    return int(factorial(n)/e + 0.5)