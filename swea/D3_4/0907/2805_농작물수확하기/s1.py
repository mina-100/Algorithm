import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    areas = [input() for _ in range(N)]
    mid = N // 2

    sum_area = 0
    for i in range(0, mid):
        for j in range(mid - i, mid + i + 1):
            sum_area += int(areas[i][j])
            sum_area += int(areas[-i-1][j])

    for k in range(N):
        sum_area += int(areas[mid][k])

    print('#{}'.format(tc), sum_area)

