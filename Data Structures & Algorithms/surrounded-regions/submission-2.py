class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        touches_edge = set()

        def dfs(r, c):
            if (
                (r < 0 or r >= ROWS) or
                (c < 0 or c >= COLS) or
                board[r][c] == "X" or
                (r, c) in touches_edge
            ):
                return        
            
            touches_edge.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] == "O" and (r, c) not in touches_edge:
                    board[r][c] = "X"




        

    