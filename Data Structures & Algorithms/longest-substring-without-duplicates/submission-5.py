class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        hs = set()

        result = 0
        for r in range(len(s)):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            result = max(result, r - l + 1)

        return result



        

