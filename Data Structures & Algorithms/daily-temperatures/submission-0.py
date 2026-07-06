class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ret = [0] * len(temperatures)
        st = []
        st.append([0, temperatures[0]])

        for i, temp in enumerate(temperatures):

            while st and temp > st[-1][1]:
                data = st.pop()
                days = i - data[0]
                ret[data[0]] = days
            st.append([i, temp])

        return ret


            



