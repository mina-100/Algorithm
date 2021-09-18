import sys
sys.stdin = open('sample_input.txt', encoding='UTF-8')

T = int(input())
for tc in range(1, 1 + T):
    N, A, B = map(int, input().split())

    min_num = A + B - N
    if min_num < 0:
        min_num = 0
    max_num = min(A, B)

    print('#{}'.format(tc), max_num, min_num)
