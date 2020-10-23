from collections import deque

# BFS on some damn randomly connected nodes. Not the same as DFS

class Node():

    def __init__(self, val, *nb, visited=False, prev=None):
        self.val = val
        self.nb = nb
        self.visited = visited
        self.prev = prev

# Generate Dict for nodes

n = {}

# Generate Nodes

for i in range(0, 13):
    n[i] = Node(i)

n[0].nb = (n[7], n[9], n[11])
n[1].nb = (n[8], n[10])
n[2].nb = (n[3], n[12])
n[3].nb = (n[2], n[4], n[7])
n[4].nb = (n[3], n[3])
n[5].nb = (n[6], n[6])
n[6].nb = (n[5], n[7])
n[7].nb = (n[3], n[6], n[0], n[11])
n[8].nb = (n[1], n[9], n[12])
n[9].nb = (n[0], n[8], n[10])
n[10].nb = (n[1], n[9])
n[11].nb = (n[0], n[7])
n[12].nb = (n[2], n[8])

# BFS is a little different to DFS. To find the shortest path via BFS, you
# Need to keep track of previous nodes. You can assign the current node to
# Non-visited nodes as its previous one, thus resulting in only one previous
# Node for each node from a specific starting point.

# All that's left is to find the desired node via BFS and backtrack through.
# Recursively/iteratively going through previous nodes of previous nodes.

# BFS makes use of a deque. The neighbors of a node are added to the deque.
# Once the node in question has been wringed of its neighbors, each neighbor
# Has their prev attribute assigned to the current node. This process repeats
# for further neighbors.


def findbybfs(start, res):
    path = []

    def bfs(start):
        q = deque()

        n[start].visited = True

        q.append(start)

        while q:
            a = q.popleft()
            for i in n[a].nb:
                if i.visited == False:
                    i.visited = True
                    q.append(i.val)
                    i.prev = n[a]
    bfs(start)
    tmp = n[res]
    while tmp != n[start]:
        path.append(tmp.val)
        tmp = tmp.prev
    path.append(start)
    print('Start: {0}, End: {1}\n{2}'.format(start, res, path[::-1]))


for i in range(13):
    for j in range(13):
        if i != j:
            findbybfs(i, j)
            for x in range(13):
                n[x].visited = False