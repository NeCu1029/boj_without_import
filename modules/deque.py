class deque:
    def __init__(self, n: int) -> None:
        self.arr = [None] * n
        self.size = n
        self.le = 0
        self.ri = 0

    def full(self) -> bool:
        return (self.ri + 1) % self.size == self.le

    def empty(self) -> bool:
        return self.le == self.ri

    def append(self, val) -> None:
        self.arr[self.ri] = val
        self.ri += 1
        self.ri %= self.size

    def appendleft(self, val) -> None:
        self.arr[self.le] = val
        self.le -= 1
        self.le %= self.size

    def pop(self):
        self.ri -= 1
        self.ri %= self.size
        return self.arr[(self.ri + 1) % self.size]

    def popleft(self):
        self.le += 1
        self.le %= self.size
        return self.arr[(self.le - 1) % self.size]
