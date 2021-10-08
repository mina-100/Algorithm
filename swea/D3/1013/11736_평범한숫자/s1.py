import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    for i in range(1, N - 1):
        sub = numbers[i - 1:i + 2]
        sub.sort()
        if sub[1] == numbers[i]:
            cnt += 1

    print('#{}'.format(tc), cnt)
