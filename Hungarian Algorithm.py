#Solving Assignment Problem through the Hungarian Method
import math

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * (self.row)  # Marking  nodes as not visited
        queue = []  # queue for BFS
        queue.append(s)  # source is visited first
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:  # if node is not visited and residual capacity > 0
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def maxflow(self, source, sink):
        parent = [-1] * (self.row)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            # updating residual capacites and reverse edges
            v = sink
            path = []
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                path.append(v)
                v = parent[v]

            path.remove(path[0])
            matches.append(path)

        return max_flow


graph = [[200, 400, 350],
         [400, 600, 350],
         [200, 400, 250]]

# Step 1
for i in range(0, len(graph)):
    m = min(graph[i])
    for j in range(0, len(graph[i])):
        graph[i][j] -= m
# Step2
for i in range(0, len(graph)):
    temp = []
    m = graph[0][i]
    for k in range(0, len(graph)):
        m = min(m, graph[k][i])
    for j in range(0, len(graph)):
        graph[j][i] -= m

# print(graph)
mb_graph = []
no_of_matches = 0

while (no_of_matches != len(graph)):
    # Step3
    n = (len(graph) * 2) + 2
    zeros = ([0] * (n-2))
    check = ([False] * (n-2))
    mb_graph = []
    matches = []
    for i in range(0, n):
        temp = ([0] * n)
        mb_graph.append(temp)
    for i in range(0, len(graph)):
        mb_graph[0][i + 1] = 1
        mb_graph[n - 1][n - 2 - i] = 1
        mb_graph[i + ((n - 2) // 2) + 1][n - 1] = 1
        for j in range(0, len(graph[i])):
            if graph[i][j] == 0:
                mb_graph[i + 1][j + ((n - 2) // 2) + 1] = 1
                zeros[i] += 1
                zeros[j+((n - 2) // 2)] += 1

    g = Graph(mb_graph)
    source = 0
    sink = n - 1
    no_of_matches = g.maxflow(source, sink)

    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            if graph[i][j] == 0:
                if zeros[i] > zeros[j+((n - 2) // 2)]:
                    check[i] = True
                elif zeros[i] < zeros[j+((n - 2) // 2)]:
                    check[j+((n - 2) // 2)] = True
                else:
                    check[i] = True
                    check[j + ((n - 2) // 2)] = True

    if no_of_matches != len(graph):
        min_value = math.inf
        for i in range(0, len(graph)):
            for j in range(0, len(graph[i])):
                if check[i] == False and check[j + ((n - 2) // 2)] == False:
                    min_value = min(graph[i][j], min_value)

        for i in range(0, len(graph)):
            for j in range(0, len(graph)):
                if check[i] == False:
                    graph[i][j] -= min_value
                if  check[j + ((n - 2) // 2)] == True:
                    graph[i][j] += min_value
    else:
        print(matches)

print(no_of_matches)
