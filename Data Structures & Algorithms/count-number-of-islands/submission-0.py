class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        islands = 0

        def bfs(r,c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()

                for rd, cd in directions:
                    r, c = row + rd, col + cd
                    if (r in range(rows) and
                        c in range(cols) and 
                        (r,c) not in visited and
                        grid[r][c] == "1"):
                        visited.add((r,c))
                        queue.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    bfs(r,c)
                    islands += 1

        return islands
