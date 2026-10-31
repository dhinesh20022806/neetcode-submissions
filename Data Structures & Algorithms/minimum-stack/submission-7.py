class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        
        if not self.stack:
            self.stack.append(val)
            self.min = val
            return
        
        self.stack.append(val - self.min)
        if self.min > val:
            self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop
        

    def top(self) -> int:
        if not self.stack:
            return -1

        print(self.stack[-1], self.min)
        if self.stack[-1] > 0:
            return  self.stack[-1] + self.min
        
        return self.min
        
        
    def getMin(self) -> int:
        if not self.stack:
            return -1

        return self.min
