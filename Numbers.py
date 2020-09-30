# Number Theory Algorithms

gcd = lambda a, b: a if b <= 0 else gcd(b, a % b)
lcm = lambda a, b: a*b/gcd(a, b)
    
def EGCD(a, b): #extended euclidean algorithm
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b != 0:
        x = a//b
        a %= b
        s0, t0 = s0 - s1*x, t0 - t1*x
        if a == 0: return b, s1, t1
        x = b//a
        b %= a
        s1, t1 = s1 - s0*x, t1 - t0*x
    return a, s0, t0
#multiplicative inverse in \Z/p\Z of k is egcd(k, p)[1]

def isPrime(n, w = False): #naive primality test
    if n in [2, 3, 5, 7]:
        return True
    for i in [2, 3, 5, 7]: 
         if n%i == 0:
            if w:
                return (False, i)
            return False
    s = int(n**0.5+1)
    for j in range(11, s, 2):
        if n%j == 0:
            if w:
                return (False, j)
            return False
    return True

def genPrime(a, b):
    if a%2 == 0:
        a += 1
    for i in range(a, b, 2):
        if isPrime(i):
            return i

def Erastothenes(n): #sieve of erastothenes
    S = [(i%2)==1 for i in range(n)]
    S[1] = False
    S[2] = True
    for i in range(3, n):
        if S[i]:
            for j in range(i**2, n, 2*i):
                S[j] = False
    return [i for i in range(n) if S[i]]
E200 = Erastothenes(200)
E500 = Erastothenes(500)
E1000 = Erastothenes(1000)
E100000 = Erastothenes(100000)

def factor(n):
    S = []
    while True:
        k = isprime(n, True)
        if k == True:
            S.append(n)
            return S
        n /= k[1]
        S.append(k[1])
    return S

def EulerPhi(n): #euler's phi (totient function)
    S = factor(n)
    for i in list(set(S)):
        n -= n/i
    return n

def getResidues(p):
    S = [-1 for i in range(p)]
    S[0]=0
    for i in range(1, p):
        S[(i**2)%p] = 1
    return S

def Legendre(q, p): #calculate legendre symbol (q/p)
        S = getresidues(p)
        k = 1
        for i in factor(q%p):
            k *= S[i]
        return k
    
def CRT(A, P): #chinese remainder theorem, x mod p_i = a_i for all i
    pr = 1
    X = 0
    for i in P:
        pr *= i
    for i in range(len(A)):
        p = pr/P[i]
        X += A[i]*egcd(p,P[i])[1]*p
    return X

def MillerRabinTest(n, a):
    r, d = 0, n-1
    while d%2 == 0: #n = (2^r)*d+1
        r += 1
        d //= 2
    x = pow(a, d, n)
    if x == 1 or x == n-1:
        return True
    for i in range(r-1):
        x = (x**2)%n
        if x == n-1:
            return True
    return False

def findBase(n): #deterministic bases for Miller-Rabin test
    if n < 2047: return [2]
    if n < 1373653: return [2, 3]
    if n < 25326001: return [2, 3, 5]
    if n < 3215031751: return [2, 3, 5, 7]
    if n < 2152302898747: return [2, 3, 5, 7, 11]
    if n < 3474749660383: return [2, 3, 5, 7, 11, 13]
    if n < 341550071728321: return [2, 3, 5, 7, 11, 13, 17]
    if n < 3825123056546413051: return [2, 3, 5, 7, 11, 13, 17, 19, 23]
    if n < 318665857834031151167461: return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n < 3317044064679887385961981: return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n < 10**337: return E200
    return E1000 #warning
    
def MillerRabin(n, B = None): #B must be a base of primes, None = auto
    if B == None:
        B = findBase(n)
    if n in B:
        return True
    for i in B:
        if MillerRabinTest(n, i) == False:
            return False
    return True
