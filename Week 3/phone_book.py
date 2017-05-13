import sys


def main():
    n = int(sys.stdin.readline().strip())

    d = {}
    for _ in range(n):
        command = sys.stdin.readline()
        if 'add' in command:
            cmd, number, name = command.split()
            d[number] = name
        elif 'del' in command:
            cmd, number = command.split()
            try:
                del d[number]
            except KeyError:
                pass
        elif 'find' in command:
            cmd, number = command.split()
            print(d.get(number, 'not found'))


if __name__ == '__main__':
    main()
