import sys
from collections import defaultdict


def hash(string, m):
    x = 263
    p = 1000000007
    res = sum(ord(char) * (x ** i) for i, char in enumerate(string))
    res %= p
    res %= m
    return res


def main():
    m = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())

    d = defaultdict(list)
    for _ in range(n):
        command, string = sys.stdin.readline().split()
        if command == 'add':
            h = hash(string, m)
            if string not in d[h]:
                d[h].append(string)
        elif command == 'del':
            h = hash(string, m)
            if string in d[h]:
                d[h].remove(string)
        elif command == 'find':
            h = hash(string, m)
            if string in d[h]:
                print('yes')
            else:
                print('no')
        elif command == 'check':
            lst = d[int(string)]
            print(' '.join(reversed(lst)))

if __name__ == '__main__':
    main()
