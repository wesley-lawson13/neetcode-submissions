class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        time = rotted = 0
        while q and rotted < fresh:
            time += 1
            level = len(q)
            for _ in range(level):
                r, c = q.popleft()
                for x, y in dirs:
                    rn, cn = r + x, c + y

                    if ((rn < 0 or rn >= ROWS) or
                        (cn < 0 or cn >= COLS) or
                        grid[rn][cn] != 1
                    ):
                        continue
                    
                    grid[rn][cn] = 2
                    rotted += 1
                    q.append((rn, cn))
        
        return time if rotted == fresh else -1
        

                    