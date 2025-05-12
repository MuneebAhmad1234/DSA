class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(n)
    mst = []

    for u, v, weight in edges:
        if ds.find(u - 1) != ds.find(v - 1):
            ds.union(u - 1, v - 1)
            mst.append((u, v, weight))
            if len(mst) == n - 1:
                break

    return mst

edges = [(1, 2, 4), (2, 3, 1), (1, 3, 3), (3, 4, 2)]
print(kruskal(edges, 4))
