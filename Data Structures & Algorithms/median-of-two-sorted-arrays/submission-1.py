class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Make A the smaller of the two arrays and calculate the total and half variables
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        # Run the binary search on the A array
        l, r = 0, len(A) - 1
        while True:
            a_mid = l + (r - l) // 2
            b_mid = half - a_mid - 2

            # Init the values to compare or make them +- inf s.t. we can safely check the values to include or not
            a_left = A[a_mid] if a_mid >= 0 else float('-inf')
            a_right = A[a_mid+1] if a_mid+1 <= len(A)-1 else float('inf')
            b_left = B[b_mid] if b_mid >= 0 else float('-inf')
            b_right = B[b_mid+1] if b_mid+1 <= len(B)-1 else float('inf')
            
            # The partition is correct - return the solution
            if a_left <= b_right and b_left <= a_right:

                if total % 2 == 1: # odd case, just return the min
                    return min(a_right, b_right)
                
                return (min(a_right, b_right) + max(a_left, b_left)) / 2
            elif a_left > b_right:
                # We have too many elements from A - need to reduce its size from the right
                r = a_mid - 1 
            else:
                l = a_mid + 1




            
        