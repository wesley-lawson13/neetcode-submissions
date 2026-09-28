class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col, pos_diag, neg_diag = set(), set(), set()

        board = [['.' for _ in range(n)] for _ in range(n)]

        ret = []

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ret.append(copy)
                return True

            for c in range(n):

                if (
                    c in col or 
                    (r + c) in pos_diag or
                    (r - c) in neg_diag
                ):
                    continue
            
                board[r][c] = "Q"
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                dfs(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return ret