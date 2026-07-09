class MinStack:

    def __init__(self):
        self.st = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if not self.st:
            self.min_val = val
            self.st.append(0)
            return

        self.st.append(val - self.min_val)
        if val < self.min_val:
            self.min_val = val

    def pop(self) -> None:
        if not self.st:
            return

        val = self.st.pop()
        if val < 0:
            self.min_val -= val

    def top(self) -> int:
        top = self.st[-1]
        if top > 0:
            return top + self.min_val
        return self.min_val

    def getMin(self) -> int:
        return self.min_val
