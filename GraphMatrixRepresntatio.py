#undirected graph
class Graph:
    def __init__(self,node):
        self.mat = list()
        for i in range(node):
            self.mat.append([0]*node)
    def add_edge(self,start,end):
        self.mat[start][end] = 1
        self.mat[end][start] = 1
    def print_graph(self):
        for i in self.mat:
            for j in i:
                print(j,end=" ")
            print()
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
    graph.print_graph()
    
