import sys
sys.stdin = open('sample_input.txt')


def padovan(x, y):
    global memo
    if x == y:
        if x < 4:
            memo[x] = 1
        else:
            memo[x] = memo[x - 3] + memo[x - 2]
    else:
        mid_num = (x + y) // 2
        padovan(x, mid_num)
        padovan(mid_num + 1, y)


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    memo = [0] * (N + 1)
    padovan(1, N)

    print('#{}'.format(tc), memo[-1])
