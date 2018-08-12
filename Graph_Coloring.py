# Graph Coloring Algorithm


def check(c, count):
    adj_edges = []
    for i in range(0, n):
        if A[count][i] == 1:
            adj_edges.append(i)
    for i in adj_edges:
        if sol[i] == c:
            return False
    return True


def color(count):
    if count == n:
        return True
    for i in chi:
        if check(i, count):
            sol[count] = i
            color(count+1)
        else:
            pass
    return False


A = [[0, 1, 0, 0, 0],     [1, 0, 1, 1, 1],     [0, 1, 0, 1, 0],     [0, 1, 1, 0, 1],     [0, 1, 0, 1, 0]]
n = len(A)

# Here, the adjacency matrix has been hard coded for convenience of testing the code
# However, you may comment out above two lines of code and use the code that has been commented below for allowing user to enter the adjacency matrix

'''
n = int(input("Enter number of nodes: "))
A = [[0]*n]*n
print("Enter 1 if an edge exists and 0 if it does not.")
for i in range(0, n):
    for j in range(0, n):
        print(i+1 , " to ", j+1, " ? : ")
        A[i][j] = int(input())
'''

chi = [str(i) for i in range(0, n)]
sol = [''] * n

for i in range(0, n):
    val = color(0)
    if val:
        break


print("Adjacency matrix: ", A)
print("Labels: ", chi)
print("Solution", sol)
print("minimum number of the colors : ", len(set(sol)))
