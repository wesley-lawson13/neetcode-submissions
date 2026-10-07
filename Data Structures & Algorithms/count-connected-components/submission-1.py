class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visited = set()
        def dfs(nd):

            if nd in visited:
                return

            visited.add(nd)
            for nei in adj[nd]:
                if nei not in visited:
                    dfs(nei)

        connected = 0
        for nd in range(n):
            if nd not in visited:
                dfs(nd)
                connected += 1

        return connected