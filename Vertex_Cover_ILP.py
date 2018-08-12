# Vertex Cover Problem through Integer Linear Programming

import pulp

'''
graph = [[0, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 1, 1],
         [0, 0, 1, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 1],
         [0, 0, 1, 1, 0, 1, 0]]

graph = [[0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 0, 1],
         [0, 1, 1, 1, 0]]
'''

graph = [[0, 1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 1, 0],
         [0, 0, 1, 0, 0, 1],
         [0, 1, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0]]


no_of_vertices = len(graph)
no_of_edges = 0
edges = []
vertices = {}

for i in range(0, no_of_vertices):
    for j in range(0, no_of_vertices):
        if i == j:
            break
        if graph[i][j] == 1:
            no_of_edges += 1
            edges.append([i, j])
    vertices[str(i)] = 0

print(edges)
p = pulp.LpProblem("Vertex Cover", pulp.LpMinimize)
var_list = {}
for i in range(0, len(vertices)):
    var_list[str(i)] = pulp.LpVariable(str(i), lowBound=0, upBound=1, cat=pulp.LpInteger)

p += sum(var_list.values()), "function"
for i in range(0, len(edges)):
    p += var_list[str(edges[i][0])] + var_list[str(edges[i][1])] >= 1

p.solve()
print(pulp.LpStatus[p.status])

for i in range(0, len(var_list)):
    print(str(i), " = ", var_list[str(i)].varValue)
print("solution = ", pulp.value(p.objective))