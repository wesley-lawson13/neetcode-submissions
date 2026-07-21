class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        pre = 1
        for i in range(1, len(nums)):
            pre *= nums[i-1]
            res[i] = pre
        
        suf = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            suf *= nums[i+1]
            res[i] *= suf

        return res
