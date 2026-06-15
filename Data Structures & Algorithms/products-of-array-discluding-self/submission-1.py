class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
                continue

            pre[i] = pre[i-1] * nums[i-1]

        suf = [0 for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suf[i] = 1
                continue

            suf[i] = suf[i+1] * nums[i+1]

        ret = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            ret[i] = pre[i] * suf[i]
        
        return ret
            


        




        