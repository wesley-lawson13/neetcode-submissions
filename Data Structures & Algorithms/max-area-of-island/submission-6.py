class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = -1 # mark visited
            
            visited = 0
            while q:
                r, c = q.popleft()
                visited += 1

                for x, y in dirs:
                    rn, cn = r + x, c + y
                    if ((rn < 0 or rn >= ROWS) or
                        (cn < 0 or cn >= COLS) or
                        grid[rn][cn] != 1
                    ):
                        continue
                    
                    q.append((rn, cn))
                    grid[rn][cn] = -1
            
            return visited
        
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area

        