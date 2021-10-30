import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    D, L, N = map(int, input().split())

    result = 0
    for i in range(N):
        result += D * (1 + (i * L / 100))

    print('#{}'.format(tc), int(result))
