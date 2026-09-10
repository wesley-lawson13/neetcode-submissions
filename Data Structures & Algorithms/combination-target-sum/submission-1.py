class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ret = []
        path = []

        def bt(i, cumSum):
            if cumSum == 0:
                ret.append(path.copy())
                return

            if i >= len(nums) or cumSum < 0:
                return

            path.append(nums[i])
            bt(i, cumSum - nums[i])

            path.pop()
            bt(i+1, cumSum)

        bt(0, target)
        return ret