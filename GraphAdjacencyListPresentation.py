
#undirected graph
class Graph:
    def __init__(self,node):
        self.l = list()
        for i in range(node):
            self.l.append(list())
    def add_edge(self,start,end):
        self.l[start].append(end)
        self.l[end].append(start)
    def print_graph(self):
        for i in range(len(self.l)):
            print("Node {} has --> {}".format(i,self.l[i]))
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
    
