import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    next_idx = 0
    cost = 0
    while len(x) > 1:
        k = len(x)
        now_x = x.pop(next_idx)
        now_y = y.pop(next_idx)
        min_L = 999999999999999999999
        for i in range(len(x)):
            now_L = (now_x - x[i]) ** 2 + (now_y - y[i]) ** 2
            if now_L <= min_L:
                min_L = now_L
                next_idx = i
        cost += min_L * E

    print('#{}'.format(tc), round(cost))

