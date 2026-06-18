class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mp1 = {}
        mp2 = {}

        for i in range(len(s)):
            
            if s[i] not in mp1:
                mp1[s[i]] = 1
            else:
                mp1[s[i]] += 1

            if t[i] not in mp2:
                mp2[t[i]] = 1
            else:
                mp2[t[i]] += 1

        return mp1 == mp2
            