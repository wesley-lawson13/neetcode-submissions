class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols = set()
        pos_diag = set() # r + c
        neg_diag = set() # r - c

        ret = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def bt(r):
            
            if r == n:
                copy = ["".join(row) for row in board]
                ret.append(copy)
                return

            for c in range(n):

                if (c in cols or
                    (r + c) in pos_diag or
                    (r - c) in neg_diag
                ):
                    continue

                board[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                bt(r + 1)

                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        bt(0)
        return ret

                
            
        