class MinStack:

    def __init__(self):
        self.st = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.st:
            self.min = val
            self.st.append(0)
            return

        self.st.append(val - self.min)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        if not self.st:
            return

        top = self.st.pop()
        if top < 0:
            self.min = self.min - top
            
    def top(self) -> int:
        
        top = self.st[-1]
        if top < 0:
            return self.min

        return top + self.min
        

    def getMin(self) -> int:
        return self.min
