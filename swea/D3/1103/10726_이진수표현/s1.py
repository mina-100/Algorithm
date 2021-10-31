import sys
sys.stdin = open('input.txt')


def is_valid(n, m):
    binary_num = format(m, '0b')
    if len(binary_num) < n:
        return 'OFF'
    for i in range(1, n + 1):
        if binary_num[-i] == '0':
            return 'OFF'
    return 'ON'


T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())

    print('#{}'.format(tc), is_valid(N, M))
