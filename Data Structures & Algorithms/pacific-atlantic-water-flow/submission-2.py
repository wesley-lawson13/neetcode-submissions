class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):

            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))

            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for x, y in dirs:
                rn, cn = r + x, c + y
                dfs(rn, cn, visit, heights[r][c])


        ROWS, COLS = len(heights), len(heights[0])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        ret = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in atl:
                    ret.append([i, j])

        return ret

        
        

                    

