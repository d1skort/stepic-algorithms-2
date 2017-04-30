import sys


sys.setrecursionlimit(20000)


def height(tree, root):
    r = 1
    for child in tree.get(root, []):
        r = max(r, height(tree, child) + 1)
    return r


def main():
    n = int(sys.stdin.readline())
    nodes = map(int, sys.stdin.readline().split())

    tree = {}
    for i, node in enumerate(nodes):
        if node == -1:
            root = i
        tree.setdefault(node, []).append(i)

    print(height(tree, root))


if __name__ == '__main__':
    main()
