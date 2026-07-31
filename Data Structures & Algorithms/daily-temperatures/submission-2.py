class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ret = [0] * len(temperatures)
        st = []

        for i, temp in enumerate(temperatures):

            while st and temp > st[-1][1]:
                prev_i, new_temp = st.pop()
                ret[prev_i] = i - prev_i
            st.append((i, temp))

        return ret

        