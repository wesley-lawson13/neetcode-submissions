class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        print(f"A: {A}, B: {B}")

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A)-1
        while True:
            mid_a = (l + r) // 2
            mid_b = half - mid_a - 2 # because of the two zero-indexed lists, need to decrement two

            a_left = A[mid_a] if mid_a >= 0 else float('-inf')
            a_right = A[mid_a+1] if mid_a+1 < len(A) else float('inf')
            b_left = B[mid_b] if mid_b >= 0 else float('-inf')
            b_right = B[mid_b+1] if mid_b+1 < len(B) else float('inf')

            if a_left <= b_right and b_left <= a_right:

                if total%2 == 1:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2

            if a_left > b_right:
                r = mid_a - 1
            else:
                l = mid_a + 1


