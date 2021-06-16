class Graph:
    def __init__(self,node):
        self.l = list()
        self.n = node
        for i in range(node):
            self.l.append(list())
            
    def add_edge(self,start,end):
        self.l[start].append(end)
        self.l[end].append(start)
        
#     def print_graph(self):
#         for i in range(len(self.l)):
#             print("Node {} has --> {}".format(i,self.l[i]))
            
    def DFSUtil(self,start,visited):
        visited[start]=True #mark true the current node
        print(start, end=" ")
        for i in range(len(self.l[start])): #explore the adjecentvia list represnataion
            if visited[self.l[start][i]] == False: #if any adjecent is false g for it and traberse graph
                self.DFSUtil(self.l[start][i],visited)
        
    def DFS(self): #start take visited array of size plus node and false it if false then go in recursion.
        visited = [False]*(self.n+1)
        for u in range(self.n):
            if visited[u] == False:
                self.DFSUtil(u,visited)
#Iterative DFS    
#     def DFS(self,start):  
#         stack = list()
#         visited = [False for i in range(self.n)]
#         stack.append(start)
#         while len(stack) > 0:
#             s = stack.pop()
#             if visited[s] == False:
#                 print(s)
#                 visited[s] = True
#             for i in self.l[s]:
#                 if visited[i] == False:
#                     stack.append(i)
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
#     graph.print_graph()
    graph.DFS()
