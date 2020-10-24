# Nothing too high-powered. Simply run a DFS on a random non-visited node.
# Append end node to a list at each function callback. Repeat until all
# Nodes are visited. The reversed list will the the topological order.

class Graph():

    def __init__(self, len):
        self.nds = [[] for i in range(len)]
        self.visited = [False for i in range(len)]

    def printGraph(self):
        print(self.nds)

    def addEdge(self, nd, nxt):
        self.nds[nd].append(nxt)

test = Graph(13)
test.printGraph()
edges = [
        (0, 3), (1, 3), (2, 0), (2, 1), (3, 6), (3, 7), (4, 0),
        (4, 3), (4, 5), (5, 9), (5, 10), (6, 8), (7, 8), (7, 9),
        (8, 11), (9, 11), (9, 12), (10, 9)
        ]

for i, j in edges:
    test.addEdge(i, j)
test.printGraph()

order = []

def dfs(index):
    global order
    for i in test.nds[index]:
        if test.visited[i] == False:
            test.visited[i] = True
            dfs(i)
            order.append(i)
        if test.visited[index] == False:
            test.visited[index] = True
            order.append(index)


for i in range(len(test.visited)):
    if test.visited[i] == False:
        dfs(i)

print(test.visited)
print(order[::-1])
