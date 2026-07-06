class MinStack:

    # Solution to store encoded values, which
    # allows you to do only need a single min value
    # instead of a stack tracking the min
    def __init__(self):
        self.st = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        # If the stack is empty, push zero,
        # indicating that the min is the val
        if not self.st:
            self.st.append(0)
            self.min_val = val
            return
        self.st.append(val - self.min_val)
        self.min_val = min(self.min_val, val)

    def pop(self) -> None:
        if not self.st:
            return 
        
        val = self.st.pop()
        if val < 0:
            self.min_val = self.min_val - val # Will be a positive change since the encoded val is neg


    def top(self) -> int:
        top = self.st[-1]
        if top > 0:
            return top + self.min_val
        return self.min_val

    def getMin(self) -> int:
        return self.min_val
