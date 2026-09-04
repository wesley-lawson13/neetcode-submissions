class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        ret = set()
        path = []

        def dfs(i, cumSum):

            if cumSum == 0:
                ret.add(tuple(path))
                return

            if i >= len(candidates) or cumSum < 0:
                return          

            # take cur and go to the next number
            path.append(candidates[i])
            dfs(i+1, cumSum - candidates[i])

            # don't take cur, go to the next UNIQUE number, hence the loop
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cumSum)

        dfs(0, target)
        return [list(path) for path in ret]