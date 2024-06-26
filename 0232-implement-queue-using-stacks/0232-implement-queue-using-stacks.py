class Stack:
    def __init__(self):
        self.items = []
    def pop(self) -> int:
        return self.items.pop()
    def push(self, x: int):
        self.items.append(x)
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        return self.items[-1]
    
class MyQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        while not self.stack1.is_empty():
            item = self.stack1.pop()
            self.stack2.push(item)
        self.stack1.push(x)
        while not self.stack2.is_empty():
            item = self.stack2.pop()
            self.stack1.push(item)

    def pop(self) -> int:
        if self.stack1.is_empty():
            return -1
        return self.stack1.pop()
        
    def peek(self) -> int:
        if self.stack1.is_empty():
            return -1
        return self.stack1.peek()        
        
    def empty(self) -> bool:
        return self.stack1.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()