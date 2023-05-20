class K_MST:
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
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


def kruskal_mst(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2]) 
    mst = []
    uf = K_MST(n)
    for edge in edges:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):
            mst.append(edge)
            uf.un(u, v)
    return mst

graph = [
    [0, 5, 0, 6, 3],
    [2, 0, 3, 8, 5],
    [4, 6, 1, 0, 7],
    [6, 3, 0, 4, 5],
    [0, 2, 4, 9, 0]
]

mst = kruskal_mst(graph)
total_weight = sum(edge[2] for edge in mst)

#Printing the path and weight
print("Minimum Spanning Tree:")
for edge in mst:
    u, v, weight = edge
    print(f"{u} -> {v} = {weight}")

print("Total Weight Of Nodes:", total_weight)