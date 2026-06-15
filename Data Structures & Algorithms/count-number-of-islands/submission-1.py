class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        from collections import deque

        count = 0
        visit = set()

        def bfs(r, c):
            
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            while q:
                row, col = q.popleft()
                for x, y in dirs:
                    r1, c1 = row + x, col + y
                    if ((r1 >= 0 and r1 < len(grid)) and 
                        (c1 >= 0 and c1 < len(grid[0])) and
                        (r1, c1) not in visit and
                        grid[r1][c1] == "1"):

                        q.append((r1, c1))
                        visit.add((r1, c1))

            return




        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if (i, j) not in visit and grid[i][j] == "1":
                    print(f"doing bfs on {i, j}...")
                    bfs(i, j)
                    print(f"visit: {visit}")
                    count += 1

        return count
