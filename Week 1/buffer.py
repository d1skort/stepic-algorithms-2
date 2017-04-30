import sys


def main():
    size, n = map(int, sys.stdin.readline().split())
    if n == 0:
        return

    packets = []
    for _ in range(n):
        arrival, duration = map(int, sys.stdin.readline().split())
        packets.append((arrival, duration))

    queue = []
    for packet in packets[:size]:
        if not queue:
            print(packet[0])
            queue.append(sum(packet))
        else:
            start = max(queue[-1], packet[0])
            print(start)
            queue.append(start + packet[1])

    for packet in packets[size:]:
        if packet[0] < queue[0]:
            print(-1)
        else:
            start = max(queue[-1], packet[0])
            queue.pop(0)
            print(start)
            queue.append(start + packet[1])

if __name__ == '__main__':
    main()
