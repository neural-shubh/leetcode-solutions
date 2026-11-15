
class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.k = k
        self.front = 0
        self.rear = -1
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.k

        self.queue[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k

        self.queue[self.rear] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.rear = (self.rear - 1) % self.k
        self.count -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
