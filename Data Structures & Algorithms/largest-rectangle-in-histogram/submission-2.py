class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        st = []

        max_area = 0
        for i, h in enumerate(heights):
            
            start = i
            while st and h < st[-1][1]:
                s, prev = st.pop()
                max_area = max(max_area, (i - s) * prev)
                start = s
            st.append((start, h))
        
        for i, h in st:
            max_area = max(max_area, (len(heights) - i) * h)
        return max_area