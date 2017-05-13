import sys


def hash(string):
    return sum(map(ord, string))


def get_text_hashes(text, window_size):

    first_window = hash(text[-window_size:])
    last_char = text[-1]

    ret = [first_window, ]

    for i in range(len(text)-window_size)[::-1]:
        last_hash = ret[-1]
        new_hash = (last_hash - ord(last_char)) + ord(text[i])
        ret.append(new_hash)
        last_char = text[i+window_size-1]
    return ret[::-1]


def main():
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()

    pattern_hash = hash(pattern)
    text_hashes = get_text_hashes(text, len(pattern))

    for i in range(len(text_hashes)):
        if text_hashes[i] == pattern_hash and text[i] == pattern[0] and text[i:i+len(pattern)] == pattern:
            print(i, end=' ')


if __name__ == '__main__':
    main()
