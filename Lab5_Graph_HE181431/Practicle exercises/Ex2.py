class WGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.weight_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, start_vertex, end_vertex, weight):
        self.weight_matrix[start_vertex][end_vertex] = weight

    def dijkstra(self, start_vertex):
        distances = [float('inf')] * self.num_vertices
        distances[start_vertex] = 0
        visited = [False] * self.num_vertices

        for _ in range(self.num_vertices):
            min_distance_vertex = self._min_distance(distances, visited)
            visited[min_distance_vertex] = True

            for vertex in range(self.num_vertices):
                if not visited[vertex] and self.weight_matrix[min_distance_vertex][vertex] != float('inf'):
                    new_distance = distances[min_distance_vertex] + self.weight_matrix[min_distance_vertex][vertex]
                    if new_distance < distances[vertex]:
                        distances[vertex] = new_distance

        return distances

    def _min_distance(self, distances, visited):
        min_distance = float('inf')
        min_distance_vertex = -1
        for vertex in range(self.num_vertices):
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_distance_vertex = vertex
        return min_distance_vertex


num_vertices = 5
graph = WGraph(num_vertices)


graph.add_edge(0, 1, 2)
graph.add_edge(0, 3, 1)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 4, 50)
graph.add_edge(2, 4, 1)
graph.add_edge(3, 2, 4)
graph.add_edge(3, 4, 3)

start_vertex = 0
shortest_distances = graph.dijkstra(start_vertex)

print(f"Shortest distances from vertex {start_vertex}: {shortest_distances}")
