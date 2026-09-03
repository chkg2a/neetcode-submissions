class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid is None or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        shortest_path = float('inf')
        memo = [[float('inf')] * cols for _ in range(rows)]
        def dfs(i,j, distance):
            nonlocal shortest_path
            if i not in range(rows) or \
               j not in range(cols) or \
               distance >= memo[i][j] or \
               distance >= shortest_path or \
               grid[i][j] == 1:
                return
            
            memo[i][j] = distance

            if i == rows - 1 and j == cols - 1 and grid[i][j] == 0:
                shortest_path = min(shortest_path, distance)
                return
            val = distance + 1
            dfs(i+1,j+1,val)
            dfs(i+1,j-1,val)
            dfs(i+1,j,val)

            dfs(i,j+1,val)
            dfs(i,j-1,val)

            dfs(i-1,j+1,val)
            dfs(i-1,j-1,val)
            dfs(i-1,j,val)
        dfs(0,0,1)
        return shortest_path if shortest_path != float("inf") else -1