# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
#Code Library
class Solution:
    def solve(self,src,order, vis,adj):
        vis[src] = True
        order[src] =True
        for i in adj[src]:
            if not vis[i]:
                flag = self.solve(i,order,vis,adj)
                if flag:
                    return True
            elif order[i]:
                return True
        order[src]=False
        return False
    def isCyclic(self, n, adj):
        vis = [False for i in range(n)]
        order = [False for i in range(n)]
        for i in range(n):
            if not vis[i]:
                flag = self.solve(i,order, vis,adj)
                if flag:
                    return True
        return False
