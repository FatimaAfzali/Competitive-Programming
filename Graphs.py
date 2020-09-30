class WeightedGraph: 
	def __init__(self, nodes, edges = None): 
		self.N = len(nodes)
		self.nodes = nodes
		self.labels = {nodes[i]: i for i in range(self.N)}
		if edges == None: 
			self.edges = [[0 for i in range(self.N)] for j in range(self.N)]
		else: 
			self.edges = edges
	def getNode(self, label): 
		return self.labels[label]
	def addNode(self, data): 
		self.nodes.append(n)
		self.N += 1
		self.labels[label] = N
		for i in self.edges: 
			i.append(0)
		self.edges.append([0] * self.N)
	def addEdge(self, label1, label2, weight): 
		self.edges[self.labels[label1]][self.labels[label2]] = weight
		self.edges[self.labels[label2]][self.labels[label1]] = weight
	def addMultipleEdges(self, L): 
		for i in L: 
			self.addEdge(i[0], i[1], i[2])
	def W(self, v, w): 
		return self.edges[self.labels[v]][self.labels[w]]
	def neighbors(self, v): 
		return [x for x in self.nodes if self.W(v, x) != 0]
	def printEdges(self): 
		for i in self.edges: 
			print(i)
	def Dijkstra(self, v): 
		N = [v] 
		nN = [x for x in self.nodes if x != v]
		D = {x: 1e9 for x in self.nodes}
		D[v] = 0
		for i in self.neighbors(v): 
			D[i] = self.W(v, i)
		while len(nN) > 0: 
			w, i = nN[0], D[nN[0]]
			for j in nN[1:]: 
				if D[j] < i: 
					w, i = j, D[j]
			N.append(w)
			nN.remove(w)
			for k in self.neighbors(w): 
				if k in nN: 
					D[k] = min([D[k], D[w] + self.W(w, k)])
		return [D[x] for x in self.nodes]

