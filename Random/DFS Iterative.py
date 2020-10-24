# DFS on some damn randomly connected nodes, with another way of making a graph. Thanks G4G.
# In their words, this is a 'directed graph using adjacency list representation'. Yeah, whatever that means

class Graph():

    def __init__(self, vert):
        # Initialise the vertices (or nodes) of the graph, mapped to the indices of adj
        self.vert = vert
        self.adj = [[] for i in range(vert)]

    def addEdge(self, vert, res):
        # Establish the numerical values of the vertices (res) connected to a specific vertex (vert) and vice versa
        self.adj[vert].append(res)
        self.adj[res].append(vert)

    # Print graph
    def pg(self):
        print(self.adj)

    def dfs(self, start):
        # Here's how this may work (in my own words). You look for any non-visited nodes and place their values on the front of the stack.
        # You take that value and find any other non-visited nodes from that point. Repeat until the whole graph is dfs'ed.
        # I think the loop will keep popping the stack once all has been visited until there is no more in it.
        # It's like some sort of queue

        visited = [False for i in range(self.vert)]

        stack = [start]

        while len(stack):
            start = stack[-1]
            stack.pop()

            if not visited[start]:
                print(start, end=' ')
                visited[start] = True

            for i in self.adj[start]:
                if not visited[i]:
                    stack.append(i)

test = Graph(5)
test.addEdge(2, 0)
test.addEdge(0, 3)
test.addEdge(3, 1)
test.addEdge(3, 4)
test.addEdge(1, 4)
test.pg()

test.dfs(0)
