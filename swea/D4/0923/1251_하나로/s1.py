import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    next_idx = -1
    L = 0
    while len(x) > 1:
        now_x = x.pop(next_idx)
        noy_y = y.pop(next_idx)
        min_L = 3000000
        for i in range(len(x)):
            now_L = ((now_x - x[i]) ** 2 + (noy_y - y[i]) ** 2) ** 0.5
            if now_L < min_L:
                min_L = now_L
                next_idx = i
        L += min_L

    print(L)

