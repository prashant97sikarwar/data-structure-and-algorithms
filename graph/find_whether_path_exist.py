from collections import defaultdict 
class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
     
    def BFS(self, s, d): 
          
        if s == d: 
            return True
              

        visited = [False]*(len(self.graph) + 1) 
  
  
        queue = [] 
        queue.append(s) 
  
        visited[s] = True
        while(queue): 
  

            s = queue.pop(0) 
  
 
            for i in self.graph[s]: 
                  

                if i == d: 
                    return True
  
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

        return False
  
def isSafe(i, j, matrix): 
    if i >= 0 and i <= len(matrix) and j >= 0 and j <= len(matrix[0]): 
        return True
    else: 
        return False
  

def is_possible(M,N): 
    s, d = None, None
    N = len(M) 
    g = Graph() 

    k = 1 
    for i in range(N): 
        for j in range(N): 
            if (M[i][j] != 0): 
  
                 
                if (isSafe(i, j + 1, M)): 
                    g.addEdge(k, k + 1) 
                if (isSafe(i, j - 1, M)): 
                    g.addEdge(k, k - 1) 
                if (isSafe(i + 1, j, M)): 
                    g.addEdge(k, k + N) 
                if (isSafe(i - 1, j, M)): 
                    g.addEdge(k, k - N) 
              
            if (M[i][j] == 1): 
                s = k 
  
                  
            if (M[i][j] == 2): 
                d = k 
            k += 1
    return g.BFS(s, d) 

