class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        prereq = { c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 states: visited, visiting (in cycle, not in the output), and unvisited

        ret = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True

            cycle.add(crs)
            for nei in prereq[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)

            visit.add(crs)
            ret.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return ret

        
            

