class Solution:
    def trap(self, height: List[int]) -> int:
        
        pre, suf = [0] * len(height), [0] * len(height)
        for i, num in enumerate(height):
            if i == 0:
                pre[i] = num
                continue
            pre[i] = max(pre[i-1], num)

        for i in range(len(height)-1, -1, -1):
            if i == len(height) - 1:
                suf[i] = height[i]
                continue
            suf[i] = max(suf[i+1], height[i])
        
        total = 0
        for i in range(len(height)):
            bound = min(pre[i], suf[i])
            total += max(0, bound - height[i])

        return total