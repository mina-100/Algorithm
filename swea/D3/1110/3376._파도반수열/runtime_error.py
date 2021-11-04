import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    padovan = [0] * (N + 1)
    padovan[1] = padovan[2] = padovan[3] = 1
    for i in range(4, N + 1):
        padovan[i] = padovan[i - 3] + padovan[i - 2]

    print('#{}'.format(tc), padovan[-1])

