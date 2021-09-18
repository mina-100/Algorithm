import sys
sys.stdin = open('input.txt')


def arrival(start=(0, 0)):
    visited = [[90000] * N for _ in range(N)]
    Q = [start]
    visited[0][0] = 0
    # 이동하기 (하, 좌, 우, 상)
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    while Q:
        x, y = Q.pop(0)
        # 갈 수 있는 길 탐색
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if visited[x][y] + matrix[new_x][new_y] < visited[new_x][new_y]:
                    visited[new_x][new_y] = visited[x][y] + matrix[new_x][new_y]
                    Q.append((new_x, new_y))
    return visited[N - 1][N - 1]


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    print('#{}'.format(tc), arrival())
