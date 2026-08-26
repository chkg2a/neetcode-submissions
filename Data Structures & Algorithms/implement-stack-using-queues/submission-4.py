class MyStack:

    def __init__(self):
        self.topEle = 0
        self.queue1 = deque()
        self.queue2 = deque()
        self.curr_ele = 0

    def push(self, x: int) -> None:
        self.queue1.append(x) 
        self.topEle = x

    def pop(self) -> int:
        self.curr_ele -= 1
        i = 0
        while i < self.curr_ele:
            i += 1
            self.queue2.append(self.queue1.popleft())
        while len(self.queue2) != 0:
            self.queue1.append(self.queue2.popleft())
        return self.topEle

    def top(self) -> int:
        return self.topEle

    def empty(self) -> bool:
        return self.curr_ele == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()