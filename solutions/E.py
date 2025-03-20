import sys


def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    s = data[0].strip()
    n = int(data[1])
    words = [data[i + 2].strip() for i in range(n)]

    mapping = {
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
        'T': '8', 'U': '88', 'V': '888',
        'W': '9', 'X': '99', 'Y': '999', 'Z': '9999'
    }

    def encode(word):
        return ''.join(mapping[ch] for ch in word)

    trie = {}
    for word in words:
        code = encode(word)
        node = trie
        for ch in code:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['_w'] = word

    L = len(s)
    dp = [None] * (L + 1)
    dp[0] = (-1, "")

    for i in range(L):
        if dp[i] is None:
            continue
        node = trie
        j = i
        while j < L and s[j] in node:
            node = node[s[j]]
            j += 1
            if '_w' in node:
                if dp[j] is None:
                    dp[j] = (i, node['_w'])
    res_words = []
    idx = L
    while idx > 0:
        prev, word = dp[idx]
        res_words.append(word)
        idx = prev
    res_words.reverse()
    sys.stdout.write(' '.join(res_words))


if __name__ == '__main__':
    main()