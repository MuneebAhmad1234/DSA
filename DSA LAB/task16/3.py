class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def detect_cycle_undirected(graph):
    edges = []
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if (neighbor, node) not in edges:
                edges.append((node, neighbor))

    uf = UnionFind(graph.keys())

    for v1, v2 in edges:
        if uf.find(v1) == uf.find(v2):
            return True
        uf.union(v1, v2)

    return False

def detect_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            rec_stack.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited and dfs(neighbor):
                    return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False

if __name__ == "__main__":
    graph_undirected = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    print(detect_cycle_undirected(graph_undirected))

    graph_directed = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    print(detect_cycle_directed(graph_directed))

    graph_directed_acyclic = {
        'A': ['B'],
        'B': ['C'],
        'C': []
    }
    print(detect_cycle_directed(graph_directed_acyclic))
