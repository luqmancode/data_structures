# Stack=LIFO: Last In First Out

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def stack_size(self):
        return len(self.stack)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("size:", stack.stack_size())
print("Lastest element: ", stack.peek())
print("Popped Element: ",stack.pop())
print("Popped Element: ",stack.pop())
print("size:", stack.stack_size())
print("Lastest element: ", stack.peek())
