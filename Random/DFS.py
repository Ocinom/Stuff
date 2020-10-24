# DFS on some damn randomly connected nodes

class Node():

    def __init__(self, val, *nb, visited=False):
        self.val = val
        self.nb = (i for i in nb)
        self.visited = visited

# Generate Dict for nodes, use global variable to indicate whether value to be searched has been found

n = {}
found = False


# Generate Nodes

for i in range(0, 12):
    n[i] = Node(i)


# Gonna have to figure out a solution that does not involve duplicating nodes

n[0].nb = (n[1], n[9])
n[1].nb = (n[0], n[8])
n[2].nb = (n[3], n[3])
n[3].nb = (n[2], n[4], n[5], n[7])
n[4].nb = (n[3], n[3])
n[5].nb = (n[3], n[6])
n[6].nb = (n[5], n[7])
n[7].nb = (n[3], n[6], n[8], n[10], n[11])
n[8].nb = (n[1], n[7], n[9])
n[9].nb = (n[0], n[8])
n[10].nb = (n[7], n[11])
n[11].nb = (n[7], n[10])


# DFS is the easiest to understand from a recursive perspective. In a
# Set of nodes in a graph, the way this algorithm searches for a value
# is, as the name suggests, going all the way to one end to find the desired
# node, and if it still does not find it, it will go to another end point
# This process repeats until either there is a solution and the desired
# Node is found, or the desired node does not exist in the graph and all
# Has been searched.

# The function below first searches for all neighbors around it that have
# Not been visited. From there, it picks one neighbor and repeats this function
# Nodes are ignored when they are either visited, or a global variable
# Indicating that the solution has been found is set to True.

# Each node visited is added to the 'path' list, which is an argument in
# The function. This means that if there is a solution, the specific path
# Taken to find that solution will be found in that argument.


# DFS Function

def dfs(start, res, path=[]):
    global found
    # Return from visited nodes to prevent infinite cycles
    if n[start].visited == True:
        return
    # Nothing more needs to be done if the node to be searched for has been found
    if found == True:
        return
    # Once the node in question has been found, set global variable to True, print the path taken
    if start == res:
        print(path + [start])
        found = True
    # Each node passed through is visited
    n[start].visited = True

    # Recursively DFS through each Node
    for i in n[start].nb:
        dfs(i.val, res, path + [start])

def findbydfs(start, res):
    global found
    if not n.get(start):
        print('Invalid start node.')
        return
    for i in range(len(n)):
        n[i].visited = False
    dfs(start, res)
    if found == False:
        print('No result found')
    found = False

for i in range(10):
    for j in range(10):
        if i != j:
            findbydfs(i, j)
