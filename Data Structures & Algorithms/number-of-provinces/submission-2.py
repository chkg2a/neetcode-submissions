class DSU:
    def __init__(self,n):
        self.parent = list(range(n+1))
        self.size = [1] * (n + 1)
        self.components = n

    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        self.components -= 1
        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True

    def noOfComponents(self):
        return self.components

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    dsu.union(i,j)
        return dsu.noOfComponents()