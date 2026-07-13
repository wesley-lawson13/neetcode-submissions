class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_set = set(s1)
        s1_fs, s2_fs = [0] * 26, [0] * 26

        for c in s1:
            s1_fs[ord(c) - ord('a')] += 1 

        l = 0
        for r in range(len(s2)):
            
            c_index = ord(s2[r]) - ord('a')

            s2_fs[c_index] += 1
            if s1_fs == s2_fs:
                return True

            while s2_fs[c_index] > s1_fs[c_index]:
                s2_fs[ord(s2[l]) - ord('a')] -= 1
                l += 1

        return False