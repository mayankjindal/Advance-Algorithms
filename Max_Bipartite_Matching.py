#Maximum Bipartite Matching using Ford Fulkerson Algorithm

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

            path.remove(path[0])
            matches.append(path)

        return max_flow

bipartile_graph = {1: [5, 7],
                   2: [5, 6, 7],
                   3: [5, 6],
                   4: [7]}

left = [1, 2, 3, 4]
right = [5, 6, 7]
n = len(left) + len(right) + 2

graph = []

for i in range(0, n):
    temp = ([0]*(n))
    graph.append(temp)

for i in left:
    graph[0][i] = 1
    for j in bipartile_graph[i]:
        graph[i][j] = 1

for i in right:
    graph[n-1][i] = 1
    graph[i][n-1] = 1

g = Graph(graph)

matches = []

source = 0
sink = 8

print("Maximum matching possible = ", g.maxflow(source, sink))
print("Matches found: ")

for i in matches:
    print(i)