import time, math, sys
import matplotlib.pyplot as plt
from functools import reduce

def mean(L):
    return sum(L)/float(len(L))

def std(L):
    m = mean(L)
    return (sum([(x - m)**2 for x in L])/float(len(L)-1))**0.5

def timeit(f, L, N = 5):
    L_ = []
    for i in L:
        D = []
        for j in range(N):
            t = time.time()
            f(i)
            dt = time.time() - t
            D.append(dt)
        if N == 1:
            L_.append(mean(D))
        else: 
            L_.append((mean(D), std(D)))
    return L_

def timeplot(L, L_, logx = False, logy = False):
    m, s = [x[0] for x in L_], [x[1] for x in L_]
    if logx:
        L = [math.log(x, 10) for x in L]
    if logy:
        m = [math.log(x, 10) for x in m]
        plt.plot(L, m, '.k')
        plt.show()
        return
    plt.errorbar(L, m, yerr = s, fmt = '.k')
    plt.show()

def monoidReduce(comp, identity): 
    return lambda L: reduce(comp, L, identity)

prod = monoidReduce(lambda a, b: a*b, 1)

o = lambda *a: ((lambda *b:a[0](*b)) if len(a)==1 else lambda *b: a[0](o(*a[1:])(*b)))
lmap = o(list, map)
lmap_ = lambda f: lambda L: lmap(f, L)
sp = lambda x: lambda a: a.split(x)
cut = lambda x: lambda a: a[x:]
gather = lambda L: lambda x: L[x[0]] if len(x)==1 else gather(L[x[0]])(x[1:]) 
case = lambda L: [] if len(L) == 0 else [L[1:1+L[0][0]]]+case(L[1+L[0][0]:])
