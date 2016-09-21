class Stack:
    def __init__(self):
        self.limit = 5
        self.items = []

    def push(self, value):
        if self.is_full():
            raise StackOverflow('You can\'t add more than {} items'.format(self.limit))
        self.items.append(value)

    def peek(self):
        return self.items[::-1][0]

    def is_full(self):
        return len(self.items) == self.limit

    def pop(self):
        return self.items.pop()


class StackOverflow(Exception):
    pass
