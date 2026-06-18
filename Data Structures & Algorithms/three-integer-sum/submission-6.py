class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ret = []

        for i, num in enumerate(nums):
           
            if i > 0 and num == nums[i-1]: 
                continue

            l, r  = i + 1, len(nums) - 1
            while l < r:
                num_sum = num + nums[l] + nums[r]

                if num_sum < 0:
                    l += 1
                elif num_sum > 0:
                    r -= 1
                else:
                    ret.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        
        return ret
