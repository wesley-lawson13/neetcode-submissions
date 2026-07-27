class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freqs = {}
        mfreq = -1

        longest = 0
        l = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            mfreq = max(mfreq, freqs[s[r]])

            while (r - l + 1) - mfreq > k:
                freqs[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return max(longest, r - l + 1)