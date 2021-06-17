# Connected and disconnected graph

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
            
    # def DFSUtil(self,start,visited):
    #     visited[start]=True #mark true the current node
    #     print(start, end=" ")
    #     for i in range(len(self.l[start])): #explore the adjecentvia list represnataion
    #         if visited[self.l[start][i]] == False: #if any adjecent is false g for it and traberse graph
    #             self.DFSUtil(self.l[start][i],visited)
        
    # def DFS(self): #start take visited array of size plus node and false it if false then go in recursion.
    #     visited = [False]*(self.n+1)
    #     for u in range(self.n):
    #         if visited[u] == False:
    #             self.DFSUtil(u,visited)
# Iterative DFS code
    def DFS(self,start):
                visited = [False]*self.n

                # self.dfsRec(start, visited)
                for i in range(self.n):
                    if visited[i] == False:
                        self.dfsRec(i,visited)
    def dfsRec(self,start, visited):
        visited[start] = True
        print(start, end=" ")
        for i in self.l[start]:
            if not visited[i]:
                self.dfsRec(i, visited)
    
    def BFS(self,s,visited):
        stack = list()
        stack.append(s)
        visited[s] = True
        ans= list()
        while len(stack) > 0:
            node = stack.pop(0)
            print(node, end=" ")
            for i in self.l[node]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i]=True
    def BFSdisc(self):
        visited = [False for i in range(self.n)]
        for i in range(self.n):
            if visited[i] == False:
                self.BFS(i,visited)

if __name__ == "__main__":
    V = 7
    graph = Graph(V)
    graph.add_edge(0, 2)
    graph.add_edge(0,1)
    graph.add_edge(3, 2)
    graph.add_edge(1, 3)
    graph.add_edge(4 , 5)
    graph.add_edge(5,6)
    graph.add_edge(6, 4)
    # graph.add_edge(5, 1)
    # graph.add_edge(6, 2)
    # graph.add_edge(6, 5)
    # graph.print_graph()
    print("DFS :",end=" ")
    graph.DFS(0)
    print()
    print("BFS :",end=" ")
    graph.BFSdisc()
