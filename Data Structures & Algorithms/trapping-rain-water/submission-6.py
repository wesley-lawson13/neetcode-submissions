class Solution:
    def trap(self, height: List[int]) -> int:    

        total = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        while l < r:

            if height[l] < height[r]:
                l += 1
                max_l = max(max_l, height[l])
                total += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                total += max_r - height[r]

        return total

