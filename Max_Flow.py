#Finding the maximum flow possible using the Ford-Fulkerson Algorithm through BFS

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
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = [[0, 10, 8, 0, 0, 0],
         [0, 0, 2, 5, 0, 0],
         [0, 0, 0, 0, 10, 0],
         [0, 0, 0, 0, 0, 7],
         [0, 0, 0, 8, 0, 10],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

print("Max Flow = ", g.maxflow(source, sink))