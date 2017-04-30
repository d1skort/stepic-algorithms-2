import sys


def main():
    n = int(sys.stdin.readline())
    queries = [sys.stdin.readline().strip() for _ in range(n)]

    stack1 = []
    stack2 = []

    for query in queries:
        if query.startswith('push'):
            value = int(query.split()[1])
            if not stack1:
                stack2.append(value)
            else:
                stack2.append(max(value, stack2[-1]))
            stack1.append(value)
        elif query == "pop":
            stack1.pop()
            stack2.pop()
        elif query == "max":
            print(stack2[-1])


if __name__ == '__main__':
    main()
