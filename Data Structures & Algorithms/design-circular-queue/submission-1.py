class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.k = k
        self.front = 0
        self.rear = 0

    #  f   r
    # [-1,-1,-1]
    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] == -1:
            self.q[self.rear] = value
            return True
        next_r = (self.rear + 1) % self.k
        if self.q[next_r] != -1:
            return False
        self.rear = next_r
        self.q[self.rear] = value
        return True

    #   f  f   r
    # [-1,2,3]
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        next_f = (self.front + 1) % self.k
        if self.q[next_f] == -1:
            popped = self.q[self.front]
            self.q[self.front] = -1
            return True
        popped = self.q[self.front]
        self.q[self.front] = -1
        self.front = next_f
        return True
        
    def Front(self) -> int:
        return self.q[self.front]

    def Rear(self) -> int:
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.q[self.front] == -1

    def isFull(self) -> bool:
        next_r = (self.rear + 1) % self.k
        return self.q[next_r] != -1


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()