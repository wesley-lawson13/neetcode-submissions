class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0]) 
        
        def dfs(r, c, w_idx):
            
            if w_idx == len(word):
                return True
            
            if ((r < 0 or r >= ROWS) or
                (c < 0 or c >= COLS) or
                board[r][c] == "#" or
                board[r][c] != word[w_idx]
            ):
                return False

            board[r][c] = "#"
            res = (dfs(r - 1, c, w_idx + 1)
                or dfs(r + 1, c, w_idx + 1)
                or dfs(r, c - 1, w_idx + 1)
                or dfs(r, c + 1, w_idx + 1)
            )
            board[r][c] = word[w_idx]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

            

            