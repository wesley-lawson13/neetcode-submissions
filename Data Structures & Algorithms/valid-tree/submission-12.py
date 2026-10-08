class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) >= n:
            return False

        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visit = set()
        def dfs(nd, par):

            if nd in visit:
                return False

            visit.add(nd)
            for nei in adj[nd]:
                if nei == par:
                    continue
                
                dfs(nei, nd)

            return True

        dfs(0, -1)
        return len(visit) == n
