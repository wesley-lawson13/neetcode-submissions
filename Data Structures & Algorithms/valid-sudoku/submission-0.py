class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_sets, col_sets = defaultdict(set), defaultdict(set)
        sub_boxes = defaultdict(set)

        for x in range(9):
            for y in range(9):
                num = board[x][y]
                if num in row_sets[x] or num in col_sets[y] or num in sub_boxes[(x // 3, y // 3)]:
                    return False

                if num != ".":
                    row_sets[x].add(num)
                    col_sets[y].add(num)
                    sub_boxes[(x // 3, y // 3)].add(num)
        
        
        return True
                
