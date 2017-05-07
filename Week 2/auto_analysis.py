import sys


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent, rank):
    rx, ry = find(x, parent), find(y, parent)
    if rx != ry:
        if rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[rx] = ry
            if rank[rx] == rank[ry]:
                rank[ry] += 1


def main():
    n, e, d = map(int, sys.stdin.readline().split())

    parent = [i for i in range(n)]
    rank = [1 for i in range(n)]

    for _ in range(e):
        xi, xj = map(int, sys.stdin.readline().split())
        union(xi-1, xj-1, parent, rank)

    answer = 1
    for _ in range(d):
        xi, xj = map(int, sys.stdin.readline().split())
        if find(xi-1, parent) == find(xj-1, parent):
            answer = 0
            break

    print(answer)


if __name__ == '__main__':
    main()
