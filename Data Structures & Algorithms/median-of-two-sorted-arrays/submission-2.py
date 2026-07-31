class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # First, set A to the smaller of the two arrays
        A, B, = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        # Perform binary search on A for the window
        l, r = 0, len(A) - 1
        while True:

            a_mid = (l + r) // 2
            b_mid = half - a_mid - 2

            a_left = A[a_mid] if a_mid >= 0 else float('-inf')
            a_right = A[a_mid+1] if a_mid+1 <= len(A) - 1 else float('inf')
            b_left = B[b_mid] if b_mid >= 0 else float('-inf')
            b_right = B[b_mid+1] if b_mid+1 <= len(B) - 1 else float('inf')

            # partition is correct, can return the median
            if a_left <= b_right and b_left <= a_right:

                if total % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2

                return min(a_right, b_right)
            elif a_left > b_right:
                r = a_mid - 1
            else:
                l = a_mid + 1

        


