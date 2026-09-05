class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        ret = []
        path = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                ret.append(path[::])
                return

            # All subsets that include nums[i]
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
        
            dfs(i + 1)
        
        dfs(0)
        return ret