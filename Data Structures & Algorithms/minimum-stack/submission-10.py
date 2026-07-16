class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.st = []

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
        if top < 0: # dealing with the min
            self.min = self.min - top

    def top(self) -> int:
        
        if self.st[-1] < 0:
            return self.min
        
        return self.min + self.st[-1]

    def getMin(self) -> int:
        return self.min
        
