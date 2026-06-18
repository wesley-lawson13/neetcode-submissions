class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ret = [0] * len(nums)

        pre = 1
        for i in range(len(nums)):
            ret[i] = pre
            pre *= nums[i]

        suf = 1
        for i in range(len(nums)-1, -1, -1):
            ret[i] *= suf
            suf *= nums[i]

        return ret