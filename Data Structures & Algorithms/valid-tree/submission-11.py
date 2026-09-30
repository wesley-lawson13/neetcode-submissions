class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != (n - 1):
            return False

        # start at any node. Then, dfs traverse, mark that node visited.
        # If the node is already visited, return false. Once you get to the end of the dfs, return True. Then, check to ensure all nodes have been visited (iterate over the nodes)

        # time complexity: O(v + e) = O(n + (n - 1)) = O(n) for the dfs, O(n) for the visited check. Space complexity is also O(n)


        adj = [[] for _ in range(n)]

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        # two sets: visited = visited on a previous DFS pass, visiting = currently being visited in this cycle
        visiting = set()
        def dfs(nd, prev):
            
            if nd in visiting:
                return False

            visiting.add(nd)
            for nei in adj[nd]:
                
                if nei == prev:
                    continue
    
                if not dfs(nei, nd):
                    return False

            return True

        return dfs(0, -1) and len(visiting) == n

        



