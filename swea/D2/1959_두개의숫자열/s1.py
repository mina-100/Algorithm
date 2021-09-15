import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    # 더 긴 리스트 찾기
    short = N_list
    long = M_list
    if len(N_list) > len(M_list):
        short = M_list
        long = N_list

    max_sum = 0
    for j in range(len(long) - len(short) + 1):
        i = 0
        multi_sum = 0
        for k in range(j, j + len(short)):
            multi_sum += (short[i] * long[k])
            i += 1
        if multi_sum > max_sum:
            max_sum = multi_sum

    print('#{} {}'.format(tc, max_sum))

