class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        st = []
        left_bound = [-1] * n
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                left_bound[i] = st[-1]
            st.append(i)

        st = []
        right_bound = [n] * n
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                right_bound[i] = st[-1]
            st.append(i)

        max_area = 0
        for i in range(n):
            left_bound[i] += 1
            right_bound[i] -= 1
            max_area = max(max_area, heights[i] * (right_bound[i] - left_bound[i] + 1))
        return max_area


            
            


