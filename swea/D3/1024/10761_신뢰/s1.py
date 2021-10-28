import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    arr = list(input().split())
    N = int(arr[0])

    before_posi = 1
    time = 0
    for i in range(1, N + 1):
        color, posi = arr[2 * i - 1], int(arr[2 * i])
        if color == 'O':
            if posi < before_posi:
                time += (before_posi - posi + 1)
                before_posi = posi
            