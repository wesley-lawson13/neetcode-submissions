class MinStack:

    def __init__(self):
        self.st = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.st.append(val)
        new_min = min(val, self.min_val[-1] if self.min_val else val)
        self.min_val.append(new_min)

    def pop(self) -> None:
        self.min_val.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
