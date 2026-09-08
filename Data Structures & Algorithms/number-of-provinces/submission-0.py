class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        n = len(isConnected)
        self.visited = [False] * n
        def dfs(node):
            
            self.visited[node] = True
            for nei in range(n):
                if not self.visited[nei] and isConnected[node][nei]:
                    dfs(nei)
        
        for i in range(n):
            if not self.visited[i]:
                dfs(i)
                res += 1
        return res