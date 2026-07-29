class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if target == nums[mid]: 
                return mid
            
            # sorted side
            if nums[l] <= nums[mid]:

                # is in the range:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:

                # if target is in the range of the right side
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
