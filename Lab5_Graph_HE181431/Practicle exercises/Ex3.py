class WGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.weight_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, start_vertex, end_vertex, weight):
        self.weight_matrix[start_vertex][end_vertex] = weight
        self.weight_matrix[end_vertex][start_vertex] = weight

    def prim_mst(self):
        included = [False] * self.num_vertices
        min_weights = [float('inf')] * self.num_vertices

        min_weights[0] = 0

        for _ in range(self.num_vertices):
            min_weight_vertex = self._min_weight_vertex(included, min_weights)
            included[min_weight_vertex] = True

            for vertex in range(self.num_vertices):
                if not included[vertex] and self.weight_matrix[min_weight_vertex][vertex] < min_weights[vertex]:
                    min_weights[vertex] = self.weight_matrix[min_weight_vertex][vertex]

        return min_weights

    def _min_weight_vertex(self, included, min_weights):
        min_weight = float('inf')
        min_weight_vertex = -1
        for vertex in range(self.num_vertices):
            if not included[vertex] and min_weights[vertex] < min_weight:
                min_weight = min_weights[vertex]
                min_weight_vertex = vertex
        return min_weight_vertex


num_vertices = 5
graph = WGraph(num_vertices)

graph.add_edge(0, 1, 2)
graph.add_edge(0, 3, 1)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 4, 1)
graph.add_edge(3, 2, 4)
graph.add_edge(3, 4, 3)

min_spanning_tree_weights = graph.prim_mst()

print(f"Minimum Spanning Tree Weights: {min_spanning_tree_weights}")
