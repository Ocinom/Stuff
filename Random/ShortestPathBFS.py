# Find shortest distance between nodes. WIP

# Not the best graph out there. Definitely limited in functionality. Edges can be added anywhere but the problem comes when you have to insert
# vertices in the middle of the graph. For the sake of simplicity, and to test out a concept, we'll just leave the graph at that.
class Graph():
    
    # Initalise graph w/ total number of vertices
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[] for i in range(vertices)]
    
    # Get length of graph i.e. number of vertices
    def __len__(self):
        return len(self.adj)
        
    # Create connections between vertices    
    def addEdge(self, start, end):
        mx = len(self.adj) - 1
        if start > mx or end > mx or start < 0 or end < 0:
            print('Invalid values added.')
            return
        self.adj[start].append(end)
        self.adj[end].append(start)
        
    def printGraph(self):
        print('[')
        for i in self.adj:
            print(i)
        print(']')
        
    def findShortestPath(self, start, end):
        from collections import deque
        
        visited = [False for i in range(self.vertices)]
        prev = [False for i in range(self.vertices)]
        
        def bfs(start):
            q = deque()
            q.append(start)
            
            while q:
                select = q.popleft()
                for i in self.adj[select]:
                    if visited[i] == False:
                        visited[i] = True
                        q.append(i)
                        prev[i] = select
        bfs(start)
        cur = end
        path = []
        while cur != start:
            path.append(cur)
            cur = prev[cur]
        print([cur] + path[::-1])
            
g = Graph(8)

edges = [
    (0, 1), (0, 3), (1, 3), (2, 3), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6)
]

for i, j in edges:
    g.addEdge(i, j)
    
# g.findShortestPath(4, 7)  returns [4, 3, 2, 7]
