class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left_max, right_max = height[0], height[-1]

        l, r = 0, n-1
        total = 0
        while l < r:

            if left_max < right_max:
                l += 1
                left_max = max(height[l], left_max)
                total += left_max - height[l]
            else:
                r -= 1
                right_max = max(height[r], right_max)
                total += right_max - height[r]
            
        return total