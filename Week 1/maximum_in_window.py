import sys

class MaximumStack:
    def __init__(self):
        self.items = []
        self.maximums = []

    def append(self, value):
        if not self.items:
            self.maximums.append(value)
        else:
            self.maximums.append(max(value, self.maximums[-1]))
        self.items.append(value)

    def pop(self):
        self.maximums.pop()
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def get_max(self):
        return self.maximums[-1]


class MaximumQueue:
    def __init__(self):
        self.instack = MaximumStack()
        self.outstack = MaximumStack()

    def enqueue(self, value):
        self.instack.append(value)

    def dequeue(self):
        if self.outstack.is_empty():
            while not self.instack.is_empty():
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def get_max(self):
        if self.instack.is_empty() or self.outstack.is_empty():
            current_max = self.outstack.get_max() if self.instack.is_empty() else self.instack.get_max()
        else:
            current_max = max(self.instack.get_max(), self.outstack.get_max())
        return current_max


def main():
    n = int(sys.stdin.readline())
    array = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())

    queue = MaximumQueue()
    ret = []

    for i, item in enumerate(array):
        queue.enqueue(item)
        if i >= (m - 1):
            print(queue.get_max(), end=' ')
            queue.dequeue()
    print()

if __name__ == '__main__':
    main()
