class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m, n = len(grid), len(grid[0])
        INF = 2 ** 31 - 1
        
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            r, c = q.popleft()
            for x, y in dirs:
                rn, cn = r + x, c + y
                if (
                    (rn < 0 or rn >= m) or
                    (cn < 0 or cn >= n) or
                    (grid[rn][cn] != INF)
                ):
                    continue

                grid[rn][cn] = grid[r][c] + 1
                q.append((rn, cn))

        



            