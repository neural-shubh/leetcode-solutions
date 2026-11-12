class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        pass

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        pass

    def top(self) -> int:
        return self.stack[-1]
        pass

    def getMin(self) -> int:
        return self.min_stack[-1]
        pass