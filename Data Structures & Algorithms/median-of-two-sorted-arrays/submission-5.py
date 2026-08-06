class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A)-1
        while True:

            mid_a = (r + l) // 2
            mid_b = half - mid_a - 2

            a_left = A[mid_a] if mid_a >= 0 else float('-inf')
            a_right = A[mid_a+1] if mid_a+1 < len(A) else float('inf')
            b_left = B[mid_b] if mid_b >= 0 else float('-inf')
            b_right = B[mid_b+1] if mid_b+1 < len(B) else float('inf')

            if a_left <= b_right and b_left <= a_right:

                """if odd, take the min of the rights"""
                if total % 2 == 1:
                    return min(a_right, b_right)
                
                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            if a_left > b_right:
                """The window on the smaller array is too large: Needs
                    to decreased by updating the right pointer
                """
                r = mid_a - 1
            else:
                """The window on the smaller array should be larger, need to update
                    the left pointer to look at more values, essentially taking the 
                    values to the left of it
                """
                l = mid_a + 1
        
