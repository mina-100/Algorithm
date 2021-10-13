import sys
sys.stdin = open('sample_input.txt')


def is_valid(x, y, numbers):
    for number in numbers:
        if y == number[1]:
            return False
    for number in numbers:
        if abs(number[0] - x) == abs(number[1] - y):
            return False
    return True


def queen(row, visited):
    global cnt
    if row == N:
        cnt += 1
        return

    for col in range(N):
        if is_valid(row, col, visited):
            visited.append((row, col))
            queen(row + 1, visited)
            visited.pop()


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    checked = [False] * N

    cnt = 0
    if N == 1:
        cnt = 1
    else:
        queen(0, [])

    print('#{}'.format(tc), cnt)
