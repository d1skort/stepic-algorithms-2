import sys


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent, rank, size):
    rx, ry = find(x, parent), find(y, parent)
    if rx != ry:
        if rank[rx] > rank[ry]:
            parent[ry] = rx
            size[rx] += size[ry]
            return size[rx]
        else:
            parent[rx] = ry
            if rank[rx] == rank[ry]:
                rank[ry] += 1
            size[ry] += size[rx]
            return size[ry]
    return size[rx]


def main():
    n, m = map(int, sys.stdin.readline().split())
    size = list(map(int, sys.stdin.readline().split()))

    parent = [i for i in range(n)]
    rank = [1 for i in range(n)]
    max_rows = max(size)

    for _ in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        rows = union(destination-1, source-1, parent, rank, size)
        max_rows = max(rows, max_rows)
        print(max_rows)


if __name__ == '__main__':
    main()
