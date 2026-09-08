class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ret = []
        path = []

        def bt(opens, close):

            if opens == close == n:
                ret.append(''.join(path.copy()))
                return

            if opens < n:
                path.append('(')
                bt(opens + 1, close)
                path.pop()
            if close < opens:
                path.append(')')
                bt(opens, close + 1)
                path.pop()

        bt(0, 0)
        return ret

