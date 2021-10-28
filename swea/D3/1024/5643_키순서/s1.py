import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, M = int(input()), int(input())
    heights = [list(map(int, input())) for _ in range(M)]

    check = [[-1] * N for _ in range(N)]
    # 키가 더 크면 1, 작으면 0,
    for _ in range(M):
        a, b = map(int, input())
        check[a][b] = 1
        check[b][a] = 0
    
