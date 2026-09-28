class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ret = []
        path = []

        def bt(i):
            if i >= len(s):
                ret.append(path.copy())
                return

            for j in range(i, len(s)):
                if self.is_pali(s, i, j):
                    path.append(s[i : j + 1])
                    bt(j + 1)
                    path.pop()            
        
        bt(0)
        return ret


    def is_pali(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


        