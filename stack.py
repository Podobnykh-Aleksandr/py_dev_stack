
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)


stack = Stack()
print(stack.is_empty())  # True
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.is_empty())  # False
print(stack.size())  # 3
print(stack.peek())  # 3
print(stack.pop())  # 3
print(stack.size())  # 2
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.is_empty())  # True
