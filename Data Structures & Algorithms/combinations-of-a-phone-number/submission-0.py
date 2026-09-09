class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ret = []
        path = []

        num_mp = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }

        def bt(i):

            if i >= len(digits):
                if path:
                    ret.append(''.join(path.copy()))
                return

            for letter in num_mp[digits[i]]:
                path.append(letter)
                bt(i+1)
                path.pop()

        bt(0)
        return ret

            