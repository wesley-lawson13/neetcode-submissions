class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t:
            return ""

        t_freqs = {}
        for c in t:
            t_freqs[c] = t_freqs.get(c, 0) + 1

        window = {}
        have, need = 0, len(t_freqs)
        res, res_len = [-1, -1], float('inf')
        
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in t_freqs and window[s[r]] == t_freqs[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < res_len:
                    res, res_len = [l, r+1], r - l + 1
                
                window[s[l]] -= 1
                if s[l] in t_freqs and window[s[l]] < t_freqs[s[l]]:
                    have -= 1
                l += 1
            
        return s[res[0]:res[1]] if res_len != float('inf') else ""