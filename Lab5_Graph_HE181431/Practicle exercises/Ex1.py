class Graph:
    def __init__(self):
        self.a = []
        self.label = []
        self.n = 0

    def setAMatrix(self, b, m):
        self.n = m
        for row in b:
            self.a.append(row.copy())

    def setLabel(self, c):
        self.label = c

    def breadth_first_traverse(self, start_vertex):
        visited_vertex = [False] * self.n
        queue = [start_vertex]
        visited_vertex[start_vertex] = True

        while queue:
            current_vertex = queue.pop(0)
            print(self.label[current_vertex], end = " ")

            for next_vertex in range(self.n):
                if self.a[current_vertex][next_vertex] and not visited_vertex[next_vertex]:
                    queue.append(next_vertex)
                    visited_vertex[next_vertex] = True

    def depth_first_traverse(self, start_vertex):
        visited_vertex = [False] * self.n
        self.dfs(start_vertex, visited_vertex)

    def dfs(self, vertex, visited_vertex):
        print(self.label[vertex], end = " ")
        visited_vertex[vertex] = True

        for next_vertex in range(self.n):
            if self.a[vertex][next_vertex] and not visited_vertex[next_vertex]:
                self.dfs(next_vertex, visited_vertex)


with open('figure1.txt', 'r') as file:

    adjacency_matrix = [list(map(int, line.split())) for line in file.readlines()]
print("Adjacency Matrix:")
for row in adjacency_matrix:
    print(" ".join(map(str, row)))


