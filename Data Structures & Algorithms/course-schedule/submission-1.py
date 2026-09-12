class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_mp = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_mp[crs].append(pre)

        visit = set()
        def dfs(crs):

            if crs in visit:
                return False

            if pre_mp[crs] == []:
                return True

            visit.add(crs)
            for pre in pre_mp[crs]:
                if not dfs(pre):
                    return False  
            visit.remove(crs)
            pre_mp[crs] = []
            
            return True

        # loop for not connected graphs
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True


            
        

        