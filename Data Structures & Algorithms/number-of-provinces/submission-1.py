class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        n = len(isConnected)
        self.visited = [False] * n
        for i in range(n):
            if not self.visited[i]:
                res += 1
                queue = deque()
                queue.append(i)
                while queue:
                    ele = queue.popleft()
                    self.visited[ele] = True
                    for nei in range(n):
                        if isConnected[ele][nei] and not self.visited[nei]:
                            queue.append(nei)

        return res