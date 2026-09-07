class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ret = []
        path = []

        candidates.sort()
        def bt(i, cumSum):
            if cumSum == 0:
                ret.append(path[::])
                return

            if i >= len(candidates) or cumSum < 0:
                return

            path.append(candidates[i])
            bt(i+1, cumSum - candidates[i])
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            bt(i+1, cumSum)

        bt(0, target)
        return ret
                