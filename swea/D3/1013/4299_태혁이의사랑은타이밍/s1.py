import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    D, H, M = map(int, input().split())
    d, h, m = 11, 11, 11

    temp = 24 * 60 * (d - 1) + 60 * h + m
    result = 0
    if D - d == 0 and H <= h and M < m:
        result = -1
    elif D - d == 0 and H < h:
        result = -1
    else:
        result = 60 * 24 * (D - 1) + H * 60 + M - temp

    print('#{}'.format(tc), result)
