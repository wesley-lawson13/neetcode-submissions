class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]

        ret = [0 for _ in range(n)]
        ret[0], ret[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            ret[i] = max(ret[i-2] + nums[i], ret[i-1])

        return ret[n-1]