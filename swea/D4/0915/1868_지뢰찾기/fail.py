import sys
sys.stdin = open('input.txt')


def find_mine(mines):
    global cnt
    zero = []
    for i in range(N):
        for j in range(N):
            # 아직 클릭하지 않은 곳일때,
            if not click[i][j]:
                # 지뢰일 경우
                if mines[i][j] == '*':
                    click[i][j] = True
                # 0일 경우
                elif not mines[i][j]:
                    zero.append((i, j))
                    # 클릭
                    cnt += 1
                    # 주변에 0이 있을 경우에만 연쇄적으로 터짐
                    eight_dir(i, j)
                    while next_target:
                        next_i, next_j = next_target.pop()
                        # 0이고, 클릭하지 않은 경우
                        if not mines[next_i][next_j] and not click[next_i][next_j]:
                            zero.append((next_i, next_j))
                    while zero:
                        a, b = zero.pop()
                        eight_dir(a, b)
                        while next_target:
                            next_a, next_b = next_target.pop()
                            click[next_a][next_b] = True
                            if not mines[next_a][next_b] and not click[next_a][next_b]:
                                zero.append((next_a, next_b))
    # click 하지 않은 모든 지점 체크
    for m in range(N):
        for n in range(N):
            if not click[m][n]:
                cnt += 1


def eight_dir(x, y):
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    for idx in range(8):
        if 0 <= x + dx[idx] < N and 0 <= y + dy[idx] < N:
            next_target.append((x + dx[idx], y + dy[idx]))
    return next_target


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    matrix = [input() for _ in range(N)]
    mines = [[0] * N for _ in range(N)]
    click = [[False] * N for _ in range(N)]
    next_target = []
    cnt = 0

    # 지뢰 변환
    for k in range(N):
        for l in range(N):
            if matrix[k][l] == '*':
                mines[k][l] = '*'
            else:
                eight_dir(k, l)
                while next_target:
                    next_k, next_l = next_target.pop()
                    if matrix[next_k][next_l] == '*':
                        mines[k][l] += 1

    find_mine(mines)

    print(cnt)
