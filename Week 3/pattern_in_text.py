import sys


def hash(string, x):
    p = 1000000007
    res = 0
    last_pow_x = 1
    for i, char in enumerate(string):
        res += (ord(char) * last_pow_x) % p
        last_pow_x = (last_pow_x * x) % p
    res %= p
    return res


def get_text_hashes(text, window_size, x):
    p = 1000000007

    first_window = hash(text[-window_size:], x)
    last_char = text[-1]

    ret = [first_window, ]

    for i in range(len(text)-window_size)[::-1]:
        last_hash = ret[-1]
        new_hash = ((last_hash - ord(last_char) * ((x ** (window_size-1))) % p) * x + ord(text[i])) % p
        ret.append(new_hash)
        last_char = text[i+window_size-1]
    return ret[::-1]


def main():
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()

    x = len(text)

    pattern_hash = hash(pattern, x)
    text_hashes = get_text_hashes(text, len(pattern), x)

    for i in range(len(text_hashes)):
        if text_hashes[i] == pattern_hash and text[i:i+len(pattern)] == pattern:
            print(i, end=' ')


if __name__ == '__main__':
    main()
