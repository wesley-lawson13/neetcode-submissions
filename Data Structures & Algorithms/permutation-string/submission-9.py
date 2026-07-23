class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        s1_f, s2_f = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_f[ord(s1[i]) - ord('a')] += 1
            s2_f[ord(s2[i]) - ord('a')] += 1

        match = 0
        for i in range(26):
            match += 1 if s1_f[i] == s2_f[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):

            if match == 26:
                return True

            # update right pointer values and s2_f
            index = ord(s2[r]) - ord('a')
            s2_f[index] += 1
            if s2_f[index] == s1_f[index]:
                match += 1
            elif s2_f[index] - 1 == s1_f[index]: # goes over due to gaining one freq
                match -= 1
            
            # remove the left pointer val from the s2_freq set
            index = ord(s2[l]) - ord('a')
            s2_f[index] -= 1
            if s2_f[index] == s1_f[index]:
                match += 1
            elif s2_f[index] + 1 == s1_f[index]: # goes under due to losing one freq
                match -= 1
            l += 1

        return match == 26

