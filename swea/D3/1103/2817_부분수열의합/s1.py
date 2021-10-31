import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    cnt = 0
    for i in range(1 << N):
        tmp_sum = 0
        for j in range(N):
            if i & (1 << j):
                tmp_sum += numbers[j]
            if tmp_sum > K:
                break
        if tmp_sum == K:
            cnt += 1

    print('#{}'.format(tc), cnt)
