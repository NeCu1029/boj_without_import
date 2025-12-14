class deque:
    def __init__(self, n: int) -> None:
        self.arr = [None] * n
        self.size = n
        self.le = 0
        self.ri = 0

    def append(self, val) -> None:
        self.arr[self.ri] = val
        if self.le == self.ri:
            self.le -= 1
            self.le %= self.size
        self.ri += 1
        self.ri %= self.size

    def appendleft(self, val) -> None:
        self.arr[self.le] = val
        if self.le == self.ri:
            self.ri += 1
            self.ri %= self.size
        self.le -= 1
        self.le %= self.size

    def pop(self):
        self.ri -= 1
        self.ri %= self.size
        return self.arr[self.ri]

    def popleft(self):
        self.le += 1
        self.le %= self.size
        return self.arr[self.le]


input = open(0).readline

n = int(input())
a = tuple(map(int, input().split()))

q = deque(n + 5)
for i in range(1, n + 1):
    if a[-i] == 1:
        q.appendleft(i)
    elif a[-i] == 3:
        q.append(i)
    else:
        x = q.popleft()
        q.appendleft(i)
        q.appendleft(x)

l, r = q.le, q.ri
if l > r:
    r += n + 5
for i in range(l + 1, r):
    print(q.arr[i % (n + 5)], end=" ")
