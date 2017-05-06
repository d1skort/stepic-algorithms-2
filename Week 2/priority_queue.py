import sys


class PriorityQueue:
    def __init__(self):
        self.items = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.items.append(value)
        self.sift_up()

    def extract_min(self):
        result = self.items[0]
        self.items[0], self.items[-1] = self.items[-1], self.items[0]
        self.items.pop()
        self.sift_down()
        return result

    def sift_up(self):
        i = len(self.items) - 1
        while i > 0 and self.items[self.parent(i)] > self.items[i]:
            self.items[self.parent(i)], self.items[i] = self.items[i], self.items[self.parent(i)]
            i = self.parent(i)

    def sift_down(self):
        i = 0
        while True:
            left_idx, right_idx = self.left(i), self.right(i)
            smallest = i
            if left_idx < len(self.items) and self.items[left_idx] < self.items[i]:
                smallest = left_idx
            if right_idx < len(self.items) and self.items[right_idx] < self.items[smallest]:
                smallest = right_idx
            if i == smallest:
                break
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            i = smallest


def main():
    n, m = map(int, sys.stdin.readline().split())
    ts = map(int, sys.stdin.readline().split())
    queue = PriorityQueue()

    for num_proc in range(n):
        queue.insert((0, num_proc))

    for t in ts:
        time, proc = queue.extract_min()
        print("{} {}".format(proc, time))
        queue.insert((time + t, proc))


if __name__ == '__main__':
    main()
