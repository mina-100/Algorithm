import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    scores = list(map(int, input().split()))
    distribution = [0] * 101

    for score in scores:
        distribution[score] += 1

    max_score = 0
    max_num = 0
    for i in range(101):
        if max_num <= distribution[i]:
            max_score = i
            max_num = distribution[i]

    print('#{}'.format(tc), max_score)

