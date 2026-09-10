class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        path = []
        nums.sort()

        def bt(i):
            if i >= len(nums):
                ret.append(path.copy())
                return

            path.append(nums[i])
            bt(i+1)

            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            bt(i+1)
        
        bt(0)
        return ret