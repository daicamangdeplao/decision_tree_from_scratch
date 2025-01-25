class Stack:

    def __init__(self):
        self.index = 0
        self.container = []

    def push(self, el):
        self.container.append(el)
        self.index = self.index + 1

    def pop(self):
        self.index = self.index - 1
        return self.container.pop()

    def peek(self):
        return self.container[self.index - 1]

    def is_empty(self):
        return len(self.container) == 0
