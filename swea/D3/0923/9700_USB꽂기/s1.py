import sys
sys.stdin = open('sample_input.txt')


def probability(p, q, n):
    k = n // 2
    if n % 2:
        return (1 - p) * q * ((1 - q) ** k)
    else:
        return p * (1 - q) * q * ((1 - q) ** (k - 1))


T = int(input())
for tc in range(1, 1 + T):
    # p: USB 바로 꽂을 확률, q: USB 정상적으로 꽂힐 확률
    p, q = map(float, input().split())

    # s1 = (1 - p) * q
    # s2 = p * (1 - q) * q
    if probability(p, q, 2) > probability(p, q, 1):
        print('#{}'.format(tc), 'YES')
    else:
        print('#{}'.format(tc), 'NO')
