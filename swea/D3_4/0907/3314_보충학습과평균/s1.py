import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    scores = list(map(int, input().split()))
    students = 5

    sum_score = 0
    for score in scores:
        if score < 40:
            sum_score += 40
        else:
            sum_score += score

    print('#{}'.format(tc), sum_score//students)

