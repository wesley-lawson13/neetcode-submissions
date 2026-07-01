class Solution:
    def isValid(self, s: str) -> bool:
        
        
        
        from collections import deque

        mp = {'(': ')', '{': '}', '[': ']'}
        st = deque()

        for char in s:
            if char in mp.keys():
                st.append(mp[char])
                continue

            if len(st) == 0 or char != st[-1]:
                return False
            st.pop()

        return len(st) == 0


