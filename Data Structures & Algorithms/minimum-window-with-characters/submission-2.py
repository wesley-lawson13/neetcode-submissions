class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s:
            return ""

        t_freq = {}

        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1
        
        window = {}
        cover, total = 0, len(t_freq)  
        res, shortest = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):

            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in t_freq and window[s[r]] == t_freq[s[r]]:
                cover += 1

            while cover == total:
                print(f"fits: {s[l:r+1]}")
                res = [l, r+1] if r - l + 1 < shortest else res
                shortest = min(shortest, res[1] - res[0])

                window[s[l]] -= 1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    cover -= 1
                l += 1

        l, r = res[0], res[1]
        return s[l:r] if shortest != float('inf') else ""

            

            

            
            

