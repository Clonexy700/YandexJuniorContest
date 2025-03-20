import sys
import itertools
from math import ceil


def main():
    data = sys.stdin.read().splitlines()
    n, m, x, y = map(int, data[0].split())
    total_rows = n * x
    total_cols = m * y
    threshold = ceil(x * y / 2)

    cum_rows = [None] * total_rows
    for i in range(total_rows):
        row = data[i + 1].rstrip()
        row_vals = [1 if ch == 'X' else 0 for ch in row]
        cum_rows[i] = [0, *itertools.accumulate(row_vals)]

    ans = 0
    for floor in range(n):
        top = floor * x
        bottom = top + x
        for apt in range(m):
            left = apt * y
            right = left + y
            s = 0
            for i in range(top, bottom):
                s += cum_rows[i][right] - cum_rows[i][left]
            if s >= threshold:
                ans += 1

    sys.stdout.write(str(ans))


if __name__ == '__main__':
    main()
