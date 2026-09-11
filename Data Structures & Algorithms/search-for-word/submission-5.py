class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])

        def bt(r, c, w_idx):

            if w_idx == len(word):
                return True

            if ((r < 0 or r >= ROWS) or
                (c < 0 or c >= COLS) or
                board[r][c] == "#" or
                board[r][c] != word[w_idx]
            ):
                return False

            board[r][c] = "#"

            ret = (
                bt(r + 1, c, w_idx + 1) or
                bt(r, c + 1, w_idx + 1) or
                bt(r - 1, c, w_idx + 1) or
                bt(r, c - 1, w_idx + 1)
            )
            board[r][c] = word[w_idx]
            return ret

        for r in range(ROWS):
            for c in range(COLS):

                if bt(r, c, 0):
                    return True

        return False