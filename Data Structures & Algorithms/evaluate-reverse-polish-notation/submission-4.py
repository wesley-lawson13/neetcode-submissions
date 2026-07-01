class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = ["+", "/", "-", "*"]

        for token in tokens:
            if token not in ops:
                st.append(token)
                continue
            
            top, second = st.pop(), st.pop()
            match token:
                case "+":
                    st.append(int(top) + int(second))
                case "-":
                    st.append(int(second) - int(top))
                case "*":
                    st.append(int(top) * int(second))
                case "/":
                    st.append(int(float(second) / int(top)))
            
            print(f"operation: {second} {token} {top} = {st[-1]}")
            
        return int(st[0])

            
