import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    NxN = [list(map(str, input().split())) for _ in range(N)]

    rotation_NxN = [[] * 3 for _ in range(N)]

    # 90도 회전
    for j in range(N):
        result = ''
        for i in range(N - 1, -1, -1):
            result += NxN[i][j]
        rotation_NxN[j].append(result)

    # 180도 회전
    for i in range(N - 1, -1, -1):
        result = ''
        for j in range(N - 1, -1, -1):
            result += NxN[i][j]
        rotation_NxN[N - i - 1].append(result)

    # 270도 회전
    for j in range(N - 1, -1, -1):
        result = ''
        for i in range(N):
            result += NxN[i][j]
        rotation_NxN[N - j - 1].append(result)

    print('#{}'.format(tc))
    for rotation in rotation_NxN:
        print(*rotation)
