from collections import defaultdict

class Graph:
 
    def __init__(self):
 
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS_visit(self, v, visited):
        visited[v] = 1
        print(v)

        for i in self.graph[v]:
            if visited[i] == 0:
                self.DFS_visit(i, visited)

    def DFS(self, v):
        visited = [0]* len(self.graph)

        self.DFS_visit(v,visited)
        
 
g= Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
g.DFS(2)
