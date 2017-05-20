import sys


def in_order(tree, root):
    if tree[root]['left'] != -1:
        in_order(tree, tree[root]['left'])
    print(tree[root]['key'], end=' ')
    if tree[root]['right'] != -1:
        in_order(tree, tree[root]['right'])


def pre_order(tree, root):
    print(tree[root]['key'], end=' ')
    if tree[root]['left'] != -1:
        pre_order(tree, tree[root]['left'])
    if tree[root]['right'] != -1:
        pre_order(tree, tree[root]['right'])


def post_order(tree, root):
    if tree[root]['left'] != -1:
        post_order(tree, tree[root]['left'])
    if tree[root]['right'] != -1:
        post_order(tree, tree[root]['right'])
    print(tree[root]['key'], end=' ')


def main():
    n = int(sys.stdin.readline())
    tree = {}
    for i in range(n):
        key, left, right = map(int, sys.stdin.readline().split())
        tree[i] = {'key': key, 'left': left, 'right': right}

    for func in (in_order, pre_order, post_order):
        func(tree, 0)
        print()


if __name__ == '__main__':
    main()
