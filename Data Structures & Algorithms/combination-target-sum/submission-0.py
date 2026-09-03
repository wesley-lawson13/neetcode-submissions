class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        ret = []
        path = []
        def dfs(i, cumSum):

            if i >= len(nums) or cumSum < 0:
                return

            if cumSum == 0:
                ret.append(path.copy())
                return
            
            # take cur
            path.append(nums[i])
            dfs(i, cumSum - nums[i])

            # don't take cur
            path.pop()
            dfs(i+1, cumSum)

        dfs(0, target)
        return ret




            