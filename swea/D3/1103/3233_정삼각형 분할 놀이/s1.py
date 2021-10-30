import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    A, B = map(int, input().split())

    n = A // B
    result = 0
    for i in range(1, n + 1):
        result += 2 * i - 1

    print('#{}'.format(tc), result)