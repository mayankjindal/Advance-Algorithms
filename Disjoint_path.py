#Finding the disjoint paths using Ford Fulkerson Algorithm

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)

    def BFS(self, s, t, parent):
        visited = [False]*(self.row)  #Marking  nodes as not visited
        queue = []  #queue for BFS
        queue.append(s)  #source is visited first
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:  #if node is not visited and residual capacity > 0
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def maxflow(self, source, sink):
        parent = [-1]*(self.row)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            #updating residual capacites and reverse edges
            v = sink
            path = []
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                path.append(v)
                v = parent[v]

            path.append(0)
            disjoint_paths.append(path)


        return max_flow


graph = [[0, 10, 8, 0, 0, 0],
         [0, 0, 2, 5, 0, 0],
         [0, 0, 0, 0, 10, 0],
         [0, 0, 0, 0, 0, 7],
         [0, 0, 0, 8, 0, 10],
         [0, 0, 0, 0, 0, 0]]

for i in range(0, len(graph)):
    for j in range(0, len(graph[i])):
        if graph[i][j] > 0:
            graph[i][j] = 1

g = Graph(graph)

disjoint_paths = []

source = 0
sink = 5

print("Total number of disjoint paths = ", g.maxflow(source, sink))
print("The disjoint paths are: ")

for i in disjoint_paths:
    for j in range(len(i)-1 , -1, -1):
        print(i[j], end=' ')
    print("\n")