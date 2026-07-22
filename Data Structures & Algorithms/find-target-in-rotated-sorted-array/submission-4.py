class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[l] == target:
                return l
            
            if nums[r] == target:
                return r

            # check for a sorted side
            if nums[l] < nums[mid]: 
                
                # If the target is in the range of the sorted side check it
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # Doing the same thing on the other side (which is the sorted side)
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return nums[l] if nums[l] == target else -1