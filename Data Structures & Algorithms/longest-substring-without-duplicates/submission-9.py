class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        in_window = set()

        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in in_window:
                in_window.remove(s[l])
                l += 1
            
            in_window.add(s[r])
            longest = max(longest, r - l + 1)

        return longest