import sys
sys.stdin = open('input.txt')


def exponentiation(x, y):
    if x == y:
        return N
    else:
        mid_num = (x + y) // 2
        left = exponentiation(x, mid_num)
        right = exponentiation(mid_num + 1, y)
    return left * right


T = 10
for tc in range(1, 1 + T):
    number = int(input())
    N, M = map(int, input().split())
    x = 1
    y = M

    print('#{}'.format(tc), exponentiation(x, y))
