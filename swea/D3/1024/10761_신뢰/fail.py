import sys
sys.stdin = open('input.txt')


def button(O, B, N):
    time = 0
    pos_o = pos_b = 1

    while N > 0:
        time += 1
        flag = 0

        # Orange 버튼 눌러야 할 때
        if O[pos_o]:
            O[pos_o] = 0
            flag = 1
            N -= 1
        else:
            pos_o += 1

        if not flag and B[pos_b]:
            B[pos_b] = 0
            N -= 1
        elif not B[pos_b]:
            pos_b += 1

    return time


T = int(input())
for tc in range(1, 1 + T):
    arr = list(input().split())
    N = int(arr[0])

    O = [0] * 101
    B = [0] * 101

    for i in range(1, N + 1):
        if arr[2 * i - 1] == 'O':
            O[int(arr[2 * i])] = 1
        else:
            B[int(arr[2 * i])] = 1

    print(button(O, B, N))



