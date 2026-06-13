class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l, r = 0, 1
        longest = 0
        cur = 1
        while r < len(s) and l < len(s):
            seen = set(s[l])

            while  r < len(s) and s[r] not in seen:
                cur += 1
                seen.add(s[r])
                print(f"r: {s[r]}, cur: {cur}")
                r += 1
            
            longest = max(longest, cur)
            l += 1
            r = l + 1
            cur = 1
        
        return max(longest, cur)

