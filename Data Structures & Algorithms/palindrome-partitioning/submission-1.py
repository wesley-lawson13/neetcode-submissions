class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ret = []
        path = []

        def bt(j, i):
            if i >= len(s):
                if i == j:
                    ret.append(path.copy())
                return

            if self.is_pali(s, j, i):
                path.append(s[j: i + 1])
                bt(i + 1, i + 1)
                path.pop()

            bt(j, i + 1)
        
        bt(0, 0)
        return ret


    def is_pali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

            