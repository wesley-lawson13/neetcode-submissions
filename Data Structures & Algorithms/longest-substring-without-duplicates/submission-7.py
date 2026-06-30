class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        vals = set()

        l = 0
        longest = 0
        for r in range(len(s)):

            while s[r] in vals:
                vals.remove(s[l])
                l += 1

            longest = max(longest, (r - l) + 1)
            vals.add(s[r])
            print(f"longest: {longest}, r: {r}")

        return longest