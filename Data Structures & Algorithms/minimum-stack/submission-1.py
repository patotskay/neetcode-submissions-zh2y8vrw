class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        poped = []
        for i in range(len(self.stack) - 1):
            poped.append(self.stack[i])
        self.stack = poped

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        res = 10**10
        for n in self.stack:
            if res > n:
                res = n
        return res


        
