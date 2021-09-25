import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    # A, B: 빵 가격, C: 현재 금액
    A, B, C = map(int, input().split())

    x = min(A, B)
    y = max(A, B)

    bread = C // x
    extra = (C % x) // y

    print('#{}'.format(tc), bread + extra)