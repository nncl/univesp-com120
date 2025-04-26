class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
        return None

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        return None

    def empty(self):
        return not len(self.data) > 0