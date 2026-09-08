class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0]) 
        
        def dfs(r, c, w_idx, cur, seen):
            
            if cur == word:
                return True 
            
            if ((r < 0 or r >= ROWS) or
                (c < 0 or c >= COLS) or
                (r, c) in seen or
                w_idx >= len(word) or
                board[r][c] != word[w_idx]
            ):
                return False

            seen.add((r, c))
            up = dfs(r - 1, c, w_idx + 1, cur + board[r][c], seen)
            down = dfs(r + 1, c, w_idx + 1, cur + board[r][c], seen)
            left = dfs(r, c - 1, w_idx + 1, cur + board[r][c], seen)
            right = dfs(r, c + 1, w_idx + 1, cur + board[r][c], seen)
            seen.remove((r, c))
            return (up or down or left or right)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    print(f"dfs here: {board[r][c]} at {r}, {c}")
                    if dfs(r, c, 0, "", set()):
                        return True

        return False

            

            