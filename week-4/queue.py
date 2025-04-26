class Queue:
    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)

    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(0)

        return None

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

        return None

    def empty(self):
        return len(self.data) == 0