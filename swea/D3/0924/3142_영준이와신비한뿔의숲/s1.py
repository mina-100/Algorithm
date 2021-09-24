import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())

    # M = x + y
    # N = x + 2 * y
    y = N - M
    x = M - y

    print('#{}'.format(tc), x, y)
