def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))

    Q = [int(next(it)) for _ in range(n)]
    C = [int(next(it)) for _ in range(n)]
    A = int(next(it))
    B = int(next(it))
    if A == B:
        dot = A * sum(Q)
    else:
        factor = (B - A) / 255.0
        sQ = 0
        sQC = 0
        for q, c in zip(Q, C):
            sQ += q
            sQC += q * c
        dot = A * sQ + factor * (sQC + 0.5 * sQ)
        dot = int(round(dot))

    sys.stdout.write(str(dot))


if __name__ == '__main__':
    main()