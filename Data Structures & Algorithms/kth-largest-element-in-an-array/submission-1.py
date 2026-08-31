class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ## QUICK SELECT: O(n) average time complexity, O(n^2) worst case

        ## Based on a pivot point: every value in the left half
        ## is equal or less than to every value in the right half

        # Steps: 
        ## Select a pivot (the value that decides what goes in left v right half)
        ## then go through the array, putting the value in the left or right half based on the pivot value. This is done with a pivot pointer indicating the next available spot
        ### partitioning is not necessarily sorted, it just means everything on the left is less than everything on the right
        ## lastly, swap the pivot value with the value where the pivot pointer is looking at, and check whether the length - k index is the result (if this index is where the pivot pointer ended). 

    
        ret_idx = len(nums) - k

        def quick_select(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]
            
            if p > ret_idx:
                return quick_select(l, p - 1)  
            elif  p < ret_idx:
                return quick_select(p + 1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums)-1)
            


    