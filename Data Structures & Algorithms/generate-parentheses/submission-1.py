class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        ret = []
        path = []

        def bt(left, right):

            if left == right == n:
                ret.append(''.join(path.copy()))
                return

            if left < n:
                path.append('(')
                bt(left + 1, right)
                path.pop()
            if right < left:
                path.append(')')
                bt(left, right + 1)
                path.pop()

        bt(0, 0)
        return ret