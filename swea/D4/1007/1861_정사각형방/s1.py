import sys
sys.stdin = open('input.txt')


def move(positions, L):
    cnt = 1
    max_cnt = 0
    idx = L
    min_idx = 0
    while idx > 0:
        x, y = positions[idx]
        next_x, next_y = positions[idx - 1]
        if abs(x - next_x) == 1 and abs(y - next_y) == 0:
            cnt += 1
        elif abs(x - next_x) == 0 and abs(y - next_y) == 1:
            cnt += 1
        else:
            if cnt >= max_cnt:
                max_cnt = cnt
                min_idx = idx
            cnt = 1
        idx -= 1
    return min_idx, max_cnt


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    L = N ** 2
    positions = [[-1, -1]] + [0] * L
    for i in range(N):
        for j in range(N):
            positions[rooms[i][j]] = [i, j]

    print('#{}'.format(tc), *move(positions, L))


