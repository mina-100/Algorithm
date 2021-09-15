import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 수
T = int(input())
for test_case in range(1, 1+T):
    # N * N: 파리가 있는 영역
    # M * M: 파리채 사이즈
    N, M = map(int, input().split())
    fly_alive = [list(map(int, input().split())) for _ in range(N)]

    max_dead = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_dead = 0
            for row in range(i, i + M):
                for col in range(j, j + M):
                    fly_dead += fly_alive[row][col]
            if max_dead < fly_dead:
                max_dead = fly_dead

    print('#{}'.format(test_case), max_dead)

