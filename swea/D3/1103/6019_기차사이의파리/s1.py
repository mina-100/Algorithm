import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    D, A, B, F = map(int, input().split())

    time = D / (A + B)
    result = F * time

    print('#{} {}'.format(tc, result))
