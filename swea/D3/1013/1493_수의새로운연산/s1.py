import sys
sys.stdin = open('input.txt')


def find_c(a):
    for i in range(1, N):
        a -= i
        if a == 0:
            y = 1
            x = - y + (i + 1)
            return x, y
        elif a < 0:
            a += i
            x = a
            y = - x + (i + 1)
            return x, y


def find_num(a, b):
    c = a + b
    num = 0
    for j in range(1, c - 1):
        num += j
    if b == 1:
        num += c - 1
    else:
        num += a
    return num


T = int(input())
for tc in range(1, 1 + T):
    p, q = map(int, input().split())

    N = 10000000000000000

    p1, p2 = find_c(p)
    q1, q2 = find_c(q)

    print('#{}'.format(tc), find_num(p1 + q1, p2 + q2))
