class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, last):

            if ( (r < 0 or r >= ROWS) or 
                (c < 0 or c >= COLS) or
                (r, c) in visit or 
                heights[r][c] < last
            ):
                return
            
            visit.add((r, c))
            new_last = heights[r][c]
            dfs(r, c+1, visit, new_last)
            dfs(r+1, c, visit, new_last)
            dfs(r, c-1, visit, new_last)
            dfs(r-1, c, visit, new_last)

        atl, pac = set(), set()

        # Search rows-wise (so cols are incrementing)
        for y in range(COLS):
            dfs(0, y, atl, heights[0][y])
            dfs(ROWS-1, y, pac, heights[ROWS-1][y])

        # Search cols-wise (going down the rows)
        for x in range(ROWS):
            dfs(x, 0, atl, heights[x][0])
            dfs(x, COLS-1, pac, heights[x][COLS-1])

        ret = []
        # Iterate over the whole grid again and check if both visited in atlantic and pacific
        for x in range(ROWS):
            for y in range(COLS):
                if (x, y) in atl and (x, y) in pac:
                    ret.append([x, y])

        return ret


        
