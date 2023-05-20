class K_MST:
    
    #Creates two lists, parent and rank, to keep track of the parent and rank of each element in the set.
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    #Recursively finds the representative (root) of the set to which x belongs    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
    #Merges the sets to which x and y belong by making the root of one set the parent of the other. 
    #The rank is used to optimize the union operation to maintain a balanced tree structure.
    def un(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

#Function for performing the Kruskal Algo
def kruskal_mst(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2])  #Sorting edges by weight
    mst = []
    uf = K_MST(n)
    for edge in edges:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):
            mst.append(edge)
            uf.un(u, v)
    return mst

graph = [
    [0, 2, 0, 6, 3],
    [2, 0, 3, 8, 5],
    [0, 6, 0, 0, 7],
    [6, 8, 0, 0, 7],
    [0, 5, 4, 9, 0]
]

mst = kruskal_mst(graph)
total_weight = sum(edge[2] for edge in mst)

#Printing the path and weight
print("Minimum Spanning Tree:")
for edge in mst:
    u, v, weight = edge
    print(f"{u} -> {v} = {weight}")

print("Total Weight Of Nodes:", total_weight)