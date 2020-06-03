
class Graph: 

    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
  
    def DFSUtil(self, temp, v, visited): 
  
        visited[v] = True
        temp.append(v) 
        for i in self.adj[v]: 
            if visited[i] == False: 

                temp = self.DFSUtil(temp, i, visited) 
        return temp 
  
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
 
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 


from sys import *
t = int(stdin.readline())
while t > 0:
    n = int(stdin.readline())
    k = int(stdin.readline())
    g = Graph(n)
    for i in range(k):
        l,m = map(int,stdin.readline().split())
        g.addEdge(l,m)
    cc = g.connectedComponents()
    mj = len(cc)
    print(mj)
    z = []
    for i in cc:
        z.append(len(i))
    z.sort()
    for i in z:
        print(i,end=' ')
    print()
    t -= 1
        