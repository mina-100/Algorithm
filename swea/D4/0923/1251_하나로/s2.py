import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    costs = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            costs[i][j] = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) * E
            costs[j][i] = costs[i][j]

    visited = [False] * N
    min_costs = [999999999999999999] * N
    cnt = 0

    result = 0
    while cnt < N:


