class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        # 3 states: prev visited (visited in a prev path of courses), currently visiting (in our prereq path), and not visited
        visited, path = set(), set()

        ret = []
        def dfs(crs):

            if crs in visited:
                return True

            if crs in path:
                return False

            path.add(crs)
            for pre in adj[crs]:

                if not dfs(pre):
                    return False
            
            path.remove(crs)
            visited.add(crs)
            ret.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return ret