class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.colors = [0] * num_vertices

    def add_edge(self, start_vertex, end_vertex):
        self.adjacency_matrix[start_vertex][end_vertex] = 1
        self.adjacency_matrix[end_vertex][start_vertex] = 1

    def sequential_coloring(self):
        for vertex in range(self.num_vertices):
            adjacent_colors = set(self.colors[neighbor] for neighbor in range(self.num_vertices) if
                                  self.adjacency_matrix[vertex][neighbor] == 1)

            color = 1
            while color in adjacent_colors:
                color += 1

            self.colors[vertex] = color

    def print_colors(self):
        for vertex in range(self.num_vertices):
            print(f"Vertex {vertex} is colored with {self.colors[vertex]}")


num_vertices = 5
graph = Graph(num_vertices)


graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

graph.sequential_coloring()

graph.print_colors()
