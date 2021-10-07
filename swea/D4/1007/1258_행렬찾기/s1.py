import sys
sys.stdin = open('input.txt')


def find(a, b):
    global visited
    # 범위 탐색
    m = n = 1
    while matrix[a + m][b]:
        m += 1
    while matrix[a][b + n]:
        n += 1
    # 방문처리
    for mi in range(a, a + m):
        for ni in range(b, b + n):
            visited[mi][ni] = True
    return [m * n, m, n]


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    results = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if not matrix[i][j]:
                    visited[i][j] = True
                else:
                    results.append(find(i, j))

    results.sort()
    print('#{}'.format(tc), len(results), end=' ')
    for result in results:
        print(result[1], end=' ')
        print(result[2], end=' ')
    print()



