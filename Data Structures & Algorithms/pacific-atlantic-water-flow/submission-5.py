class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visit, last):

            if (
                (r < 0 or r >= ROWS) or
                (c < 0 or c >= COLS) or
                ((r, c) in visit) or
                (heights[r][c] < last)
            ):
                return

            visit.add((r, c))

            last = heights[r][c]
            dfs(r+1, c, visit, last)
            dfs(r-1, c, visit, last)
            dfs(r, c+1, visit, last)
            dfs(r, c-1, visit, last)

        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res
