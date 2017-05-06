import sys


def sift_down(lst, i):
    swaps = []
    n = len(lst)
    while True:
        left = (i + 1) * 2 - 1
        right = (i + 1) * 2
        smallest = i
        if left < n and lst[left] < lst[i]:
            smallest = left
        if right < n and lst[right] < lst[smallest]:
            smallest = right
        if i == smallest:
            break
        swaps.append((i, smallest))
        lst[i], lst[smallest] = lst[smallest], lst[i]
        i = smallest
    return swaps


def build_min_heap(lst):
    swaps = []
    for i in reversed(range(len(lst) // 2)):
        swaps.extend(sift_down(lst, i))
    return swaps


def main():
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    swaps = build_min_heap(numbers)
    print(len(swaps))
    for swap in swaps:
        print("{} {}".format(*swap))


if __name__ == '__main__':
    main()
