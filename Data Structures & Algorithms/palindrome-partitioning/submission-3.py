class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ret = []
        path = []

        def bt(l, r):
            
            if r == len(s):
                if l == r:
                    ret.append(path.copy())
                return

            if self.is_pali(s, l, r):
                path.append(s[l:r + 1])
                bt(r + 1, r + 1)
                path.pop()
            
            bt(l, r + 1)
        
        bt(0, 0)
        return ret
    
    def is_pali(self, s, l, r):

        while l < r:

            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        