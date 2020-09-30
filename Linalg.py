import math

def Identity(n): 
	arr = [[0 for i in range(n)] for j in range(n)] 
	for i in range(n): 
		arr[i][i] = 1
	return arr

def Zero(m, n): 
	return [[0 for j in range(n)] for i in range(m)]

def Angle(phi): 
	return [[math.cos(phi), -math.sin(phi)], [math.sin(phi), math.cos(phi)]]

class Matrix: 
	def __init__(self, M): 
		self.arr = M
		self.r = len(M)
		try: 
			self.c = len(M[0])
		except:
			self.arr = [M]
			self.r = 1
			self.c = len(M)
	def copy(self): 
		return Matrix(self.arr)
	def T(self): #Transpose
		return Matrix([[self.arr[j][i] for j in range(self.r)] for i in range(self.c)])
	def Tr(self): #Trace
		return sum([self.arr[i][i] for i in range(self.r)])
	def Minor(self, r, c): #Matrix minor
		M = self.arr[:r] + self.arr[r+1:]
		M = [x[:c] + x[c+1:] for x in M]
		return Matrix(M)
	def det(self): #Calculate determinant recursively
		if self.r == 1: 
			return self.arr[0][0]
		return sum([self.arr[i][0] * (-1)**(i+1) * self.Minor(i, 0).det() for i in range(self.r)])
	def Cofactor(self, r, c): 
		return self.Minor(r, c).det() * (-1)**(r+c+1)
	def Inv(self): #Calculate matrix inverse via Cramer's formula
		d = float(self.det())
		A = Zero(self.r, self.r)
		for i in range(self.r): 
			for j in range(self.r): 
				A[i][j] = self.Cofactor(i, j)/d
		return Matrix(A).T()
	def Row(self, r): 
		return Matrix([self.arr[r]])
	def Column(self, c): 
		return Matrix([self.T().arr[c]]).T()
	def Diag(self): 
		return [self.arr[i][i] for i in range(self.r)] 
	def __mul__(self, N): #Matrix multiplication, N optionally scalar
		#If result of multiplication is 1x1 matrix, returns the value as a scalar
		if type(N) in [int, float]: 
			A = Zero(self.r, self.c)
			for i in range(self.r): 
				for j in range(self.c): 
					A[i][j] = self.arr[i][j] * N
			return Matrix(A)
		MN = Zero(self.r, N.c)
		for i in range(self.r): 
			for j in range(N.c): 
				for k in range(self.c): 
					MN[i][j] += self.arr[i][k] * N.arr[k][j]
		if len(MN) == len(MN[0]) == 1: 
			return MN[0][0] 
		return Matrix(MN)
	def __rmul__(self, n): 
		return self.__mul__(n)
	def __add__(self, N): #Matrix addition; if N scalar, computes self + N*I
		M = self.copy() 
		if type(N) in [int, float]: 
			M = self.copy() 
			for i in range(self.r): 
				for j in range(self.c): 
					M.arr[i][j] += N
			return M
		for i in range(self.r): 
			for j in range(self.c): 
				M.arr[i][j] += N.arr[i][j]
		return M
	def __radd__(self, N): 
		return self.__add__(N)
	def __sub__(self, N): 
		return self.__add__(-N)
	def __pow__(self, k): #Matrix exponentiation using repeated squaring
		s = bin(k)[2:]
		MPow = self.copy()
		Acc = Matrix(Identity(self.r))
		for i in s[::-1]: 
			if i == '1': 
				Acc = Acc * MPow
			MPow *= MPow
		return Acc
	def __getitem__(self, key): 
		A = Matrix([self.arr[key]])
		if A.r*A.c == 1: 
			return A.arr[0][0]
		return A
	def __neg__(self): 
		return -1*self
	def QR(self): #QR decomposition
		U = []
		E = []
		for i in range(self.r): 
			a = self.Column(i)
			for j in range(i): 
				a -= (U[j].T()*a)*(U[j].T()*U[j])**-1*U[j]
			U.append(a.copy())
			E.append((a.copy())*(a.T()*a)**-0.5)
		Q = Zero(self.r, self.r)
		R = Zero(self.r, self.r)
		for i in range(self.r): 
			for j in range(self.r): 
				Q[i][j] = E[j][i]
				if j >= i: 
					R[i][j] = E[i].T()*self.Column(j)
		return Matrix(Q), Matrix(R)
	def Eigen(self, n = 100, err = 10**-9): #QR Algorithm
		#returns eigenvalues, number of iterations taken, convergence rate
		A = self.copy()
		for i in range(n): 
			conv = Matrix(A.Diag())
			Q, R = A.QR()
			A = R*Q
			thiserr = (Matrix(A.Diag()) - conv).Norm()
			if thiserr < err: #convergence 
				return (A.Diag(), i, thiserr)
		return (A.Diag(), i, thiserr)
	def Norm(self): #Frobenius norm, sqrt(Tr(A^T A))
		A = self.copy()
		return math.sqrt((A.T()*A).Tr())
	def __str__(self): #pretty print, taken from stackoverflow
		s = [[str(e) for e in row] for row in self.arr]
		lens = [max(map(len, col)) for col in zip(*s)]
		fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
		table = [fmt.format(*row) for row in s]
		return '\n'.join(table)

M = Matrix([[1, 0, 4], 
			[0, 2, 0], 
			[1, 1, 0]])
print(M.Eigen())
print(M.det())

