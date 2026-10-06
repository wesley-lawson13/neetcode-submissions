class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2**31 - 1

        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dist = 0
        while q:
            level = len(q)
            for _ in range(level):
                r, c = q.popleft()
                grid[r][c] = dist
                for x, y in dirs:
                    rn, cn = r + x, c + y

                    if (
                        rn < 0 or rn >= ROWS or
                        cn < 0 or cn >= COLS or
                        grid[rn][cn] != INF
                    ):
                        continue

                    grid[rn][cn] = "visit"
                    q.append((rn, cn))

            dist += 1

        

                
