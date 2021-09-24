import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    scores.sort(reverse=True)
    result = sum(scores[:K])

    print('#{}'.format(tc), result)