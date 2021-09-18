import sys
sys.stdin = open('input.txt')

# 재귀함수
# def exponentiation(n, m):
#     while m > 0:
#         if m == 1:
#             return n
#         else:
#             return n * exponentiation(n, m - 1)

memo_stack = [0] * 1000


def stack(n, m):
    if memo_stack[0] == 0:
        if m == 1:
            memo_stack[m] = n
        else:
            memo_stack[m] = n * stack(n, m - 1)
    return memo_stack[m]


T = 10
for tc in range(1, 1 + T):
    number = int(input())
    N, M = map(int, input().split())

    print('#{}'.format(), stack(N, M))


# runtime error

