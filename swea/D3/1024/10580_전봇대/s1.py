import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]

    cross = 0
    for i in range(N - 1):
        for j in range(i, N):
            if lines[i][0] < lines[j][0]:
                if lines[i][1] > lines[j][1]:
                    cross += 1
            else:
                if lines[i][1] < lines[j][1]:
                    cross += 1

    print('#{}'.format(tc), cross)
