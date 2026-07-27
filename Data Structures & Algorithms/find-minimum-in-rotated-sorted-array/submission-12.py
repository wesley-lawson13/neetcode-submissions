class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if nums[l] <= nums[mid] <= nums[r]:
                return nums[l]

            if nums[l] <= nums[mid]:
                l = mid + 1
            else: 
                r = mid

        return nums[l+1] if l else nums[0]
