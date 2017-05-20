import sys


sys.setrecursionlimit(20000)


def get_max(tree, root):
    while root != -1:
        ret = tree[root]['key']
        root = tree[root]['right']
    return ret


def get_min(tree, root):
    while root != -1:
        ret = tree[root]['key']
        root = tree[root]['left']
    return ret


def correct(tree, root):
    tree_correct = True

    root_key = tree[root]['key']
    if tree[root]['left'] != -1:
        tree_correct = root_key > get_max(tree, tree[root]['left'])
    if tree_correct and tree[root]['right'] != -1:
        tree_correct = root_key < get_min(tree, tree[root]['right'])

    if tree_correct and tree[root]['left'] != -1:
        tree_correct = correct(tree, tree[root]['left'])
    if tree_correct and tree[root]['right'] != -1:
        tree_correct = correct(tree, tree[root]['right'])

    return tree_correct


def main():
    n = int(sys.stdin.readline())
    if n == 0:
        print('CORRECT')
        return

    tree = {}
    for i in range(n):
        key, left, right = map(int, sys.stdin.readline().split())
        tree[i] = {'key': key, 'left': left, 'right': right}

    if correct(tree, 0):
        print('CORRECT')
    else:
        print('INCORRECT')


if __name__ == '__main__':
    main()
