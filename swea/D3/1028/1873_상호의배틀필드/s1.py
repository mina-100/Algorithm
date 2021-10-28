import sys
sys.stdin = open('input.txt')


def find_start(maps):
    for i in range(H):
        for j in range(W):
            if not maps[i][j] in roads:
                return i, j


def is_valid(a, b):
    return 0 <= a < H and 0 <= b < W


def battle_field(x, y):
    global maps
    for operator in operators:
        if operator == 'S':
            for tank in tanks:
                if maps[x][y] == tank[0]:
                    bomb_x, bomb_y = x, y
                    while True:
                        next_bx, next_by = bomb_x + tank[2], bomb_y + tank[3]
                        if not is_valid(next_bx, next_by):
                            break
                        else:
                            if maps[next_bx][next_by] == '*':
                                maps[next_bx][next_by] = '.'
                                break
                            elif maps[next_bx][next_by] == '#':
                                break
                            bomb_x, bomb_y = next_bx, next_by
                    break

        else:
            for tank in tanks:
                if operator == tank[1]:
                    maps[x][y] = tank[0]
                    # 다음칸이 평지면 이동
                    nx, ny = x + tank[2], y + tank[3]
                    if is_valid(nx, ny) and maps[nx][ny] == '.':
                        maps[x][y], maps[nx][ny] = maps[nx][ny], maps[x][y]
                        x, y = nx, ny


T = int(input())
for tc in range(1, 1 + T):
    H, W = map(int, input().split())
    maps = [list(input()) for _ in range(H)]
    N = int(input())
    operators = input()

    tanks = [['^', 'U', -1, 0], ['v', 'D', 1, 0], ['<', 'L', 0, -1], ['>', 'R', 0, 1]]
    roads = ['.', '*', '#', '-']
    x, y = find_start(maps)
    battle_field(x, y)

    print('#{}'.format(tc), end=' ')
    for h in range(H):
        print(''.join(maps[h]))



