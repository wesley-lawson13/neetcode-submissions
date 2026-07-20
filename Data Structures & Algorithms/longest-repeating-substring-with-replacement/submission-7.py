class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freqs = {}
        l, max_f, res = 0, 0, 0
        for r in range(len(s)):

            freqs[s[r]] = freqs.get(s[r], 0) + 1
            max_f = max(freqs[s[r]], max_f)

            while (r - l + 1) - max_f > k:
                freqs[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res