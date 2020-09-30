def LIS(S): #O(|S|^2)
	N = len(S)
	if N < 2: return N
	Ans = [1] #Ans[i] is length of LIS ending with S[i]
	for pos in range(1, N):
		#max of all cases where we can add 1, along with failsafe
		k = [Ans[x]+1 for x in range(0, pos) if S[pos] > S[x]] + [1]
		#print Ans
		Ans.append(max(k))
	#print(Ans)
	return max(Ans)

#S = [1, 9, 10, 2, 3, 4, 5, 6, 7, 2, 1, 2, 1, 2, 1, 3]
#print(LIS(S))

def LCS(S, T): #O(|S|*|T|)
	m, n = len(S), len(T)
	I = []
	SxT = [[0 for x in range(n+1)] for y in range(m+1)]
        for i in range(1, m+1):
		for j in range(1, n+1):
			if S[i-1] == T[j-1]:
				SxT[i][j] = SxT[i-1][j-1] + 1
			else:
				SxT[i][j] = max([SxT[i-1][j], SxT[i][j-1]])
	return SxT[-1][-1]

#print(LCS('3141592653', '2718281828459045')) #should be 14595

def subsetSum(S, k):
        n = len(S)
        M = [[False for x in range(k+1)] for y in range(n)]
	M[0][0] = True #trivially
	for j in S:
                M[0][j] = True
	for i in range(1,n):
                for j in range(k+1):
                        M[i][j] = M[i-1][j] or M[i-1][j-S[i]]
        #for i in M: 
        	#print([x for x in range(k+1) if i[x]])
        return M[-1][-1]

#print(subsetSum([15, 22, 14, 26, 32, 10, 16, 8], 53))

def knapsack(V, W, w): 
	n = len(V)
	M = [[0 for i in range(w+1)] for j in range(n+1)]
	for i in range(1,n+1): 
		for j in range(1,w+1): 
			if W[i-1] <= j and V[i-1] + M[i-1][j-W[i-1]] > M[i-1][j]: #avoid python's negative indexing... 
				M[i][j] = V[i-1] + M[i-1][j-W[i-1]]
			else: 
				M[i][j] = M[i-1][j]
	return M[n][w]

#V = [23.79, 41.02, 18.09, 5.06, 46.01, 2.07] 
#W = [10, 20, 10, 5, 24, 2] 
#w = 25
#print(knapsack(V, W, w)) 

def Levenshtein(S, T): 
	m, n = len(S), len(T) 
	M = [[0 for j in range(n+1)] for i in range(m+1)]
	for j in range(n+1): 
		M[0][j] = j
	for i in range(m+1): 
		M[i][0] = i
	for i in range(1,m+1): 
		for j in range(1,n+1): 
			M[i][j] = min([M[i-1][j] + 1, M[i][j-1] + 1, M[i-1][j-1] + (1-int(S[i-1] == T[j-1]))])
	return M[m][n]

#print(Levenshtein("extraneous", "neotenous")) #extraneous -> eotraneous -> neotraneous -> neoteaneous -> neoteneous -> neotenous (5)

