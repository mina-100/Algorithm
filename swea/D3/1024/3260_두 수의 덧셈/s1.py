import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    A, B = input().split()
    max_len = max(len(A), len(B))
    a, b = map(int, (A, B))

    results = [0] * (max_len + 1)
    idx = 0
    while a > 0 or b > 0:
        results[idx] += (a % 10 + b % 10)
        a, b = a // 10, b // 10
        if results[idx] >= 10:
            results[idx] -= 10
            results[idx + 1] += 1
        idx += 1

    if results[-1] == 0:
        results.pop()

    print('#{}'.format(tc), end=' ')
    for i in range(len(results)):
        print(results[- i - 1], end='')
    print()
