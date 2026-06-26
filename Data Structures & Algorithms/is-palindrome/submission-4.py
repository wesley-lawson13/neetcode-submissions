class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1

        punctuation = set(["?", " ", "!", ".", ",", "'", ":"])

        while l <= r:

            if s[l] in punctuation:
                l += 1
                continue

            if s[r] in punctuation:
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True