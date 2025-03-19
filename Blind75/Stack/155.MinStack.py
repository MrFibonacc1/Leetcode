class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        previous = self.minStack[-1] if self.minStack else float('inf')
        self.minStack.append(min(val, previous))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()



    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
