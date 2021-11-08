import sys
sys.stdin = open('sample_input.txt')


def hamburger(n, tmp_tasty, cal):
    global tasty
    if cal > L:
        return

    if tasty < tmp_tasty:
        tasty = tmp_tasty

    if n == N:
        return

    # 재료 skip
    hamburger(n + 1, tmp_tasty, cal)
    # 재료 넣기
    hamburger(n + 1, tmp_tasty + ingredients[n][0], cal + ingredients[n][1])


T = int(input())
for tc in range(1, 1 + T):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    tasty = 0
    hamburger(0, 0, 0)

    print('#{}'.format(tc), tasty)
