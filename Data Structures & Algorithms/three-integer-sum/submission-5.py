class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ## REVIEW

        # 1. Sort the array

        # 2. Use two pointers to get all valid values that can 3 sum

        ret = []
        nums.sort()

        for i, num in enumerate(nums):
            
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums)-1

            while l < r:
                total = num + nums[l] + nums[r]
                
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    ret.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1

        return ret


