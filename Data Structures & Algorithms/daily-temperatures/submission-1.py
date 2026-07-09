class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ret = [0] * len(temperatures)
        st = [] # vals: [i, temp]

        for i, temp in enumerate(temperatures):

            while st and st[-1][1] < temp:
                top = st[-1]
                ret[top[0]] = i - top[0]
                st.pop()
            st.append([i, temp])

        return ret
