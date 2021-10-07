import sys
sys.stdin = open('input.txt')


def chess(starts):
    min_change = M * N
    while starts:
        tmp_change = 0
        m, n = starts.pop()
        color = boards[m][n]
        for x in range(4):
            for y in range(4):
                if boards[m + 2 * x][n + 2 * y] != color:
                    tmp_change += 1
                if boards[m + 2 * x][n + 2 * y + 1] == color:
                    tmp_change += 1
                if boards[m + 2 * x + 1][n + 2 * y] == color:
                    tmp_change += 1
                if boards[m + 2 * x + 1][n + 2 * y + 1] != color:
                    tmp_change += 1

        if tmp_change > 32:
            tmp_change = 64 - tmp_change
        if tmp_change < min_change:
            min_change = tmp_change
    return min_change


N, M = map(int, input().split())
boards = [input() for _ in range(N)]

starts = []
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        starts.append([i, j])

print(chess(starts))