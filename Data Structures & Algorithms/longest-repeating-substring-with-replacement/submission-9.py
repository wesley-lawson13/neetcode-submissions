class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freqs = {}

        max_freq, longest = 0, 0
        l = 0
        for r in range(len(s)):

            freqs[s[r]] = freqs.get(s[r], 0) + 1
            max_freq = max(max_freq, freqs[s[r]])
            
            while (r - l + 1) - max_freq > k:       
                freqs[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest

            