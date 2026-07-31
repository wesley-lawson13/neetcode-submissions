class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(x, y):
            if ((x < 0 or x >= ROWS) or
                (y < 0 or y >= COLS) or
                (grid[x][y] == "-") or
                (grid[x][y] == "0")
            ):
                return
            
            grid[x][y] = "-"

            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for r, c in dirs:
                dfs(x+r, y+c)

        total = 0
        for x in range(ROWS):
            for y in range(COLS):

                if grid[x][y] == "1":
                    dfs(x, y)
                    total += 1

        return total

