import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    min_height = 999999999999
    for i in range(1 << N):
        if min_height == B:
            break
        height_sum = 0
        for j in range(N):
            if i & (1 << j):
                height_sum += heights[j]
        if B <= height_sum < min_height:
            min_height = height_sum
    result = min_height - B

    print('#{}'.format(tc), result)

