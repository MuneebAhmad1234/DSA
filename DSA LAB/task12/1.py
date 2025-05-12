class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}
        self.vertices = []
        self.adj_matrix = []

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.vertices.append(vertex)
            size = len(self.vertices)
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0] * size)

    def add_edge(self, start, end):
        if start not in self.adj_list or end not in self.adj_list:
            raise ValueError("Both vertices must exist in the graph.")
        
        self.adj_list[start].append(end)
        if not self.directed:
            self.adj_list[end].append(start)
        
        start_idx = self.vertices.index(start)
        end_idx = self.vertices.index(end)
        self.adj_matrix[start_idx][end_idx] = 1
        if not self.directed:
            self.adj_matrix[end_idx][start_idx] = 1

    def display_adj_list(self):
        print("Adjacency List:", self.adj_list)

    def display_adj_matrix(self):
        print("Adjacency Matrix:")
        print("  ", " ".join(self.vertices))
        for i, row in enumerate(self.adj_matrix):
            print(self.vertices[i], row)


g = Graph(directed=True)
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.display_adj_list()
g.display_adj_matrix()
