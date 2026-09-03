class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        target_idx = len(nums) - k
        def quick_select(l, r):

            pivot, p = nums[r], l
            for i in range(l, r):

                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[r], nums[p] = nums[p], nums[r]

            if p < target_idx:
                return quick_select(p + 1, r)
            elif p > target_idx:
                return quick_select(l, p - 1)
            else:
                return nums[p]

        return quick_select(0, len(nums)-1)