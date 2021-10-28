import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    costs = list(map(int, input().split()))

    costs.sort(reverse=True)
    result = sum(costs)
    for i in range(2, N, 3):
        result -= costs[i]
    print('#{}'.format(tc), result)
