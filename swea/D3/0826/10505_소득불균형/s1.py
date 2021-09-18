import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    incomes = list(map(int, input().split()))

    sum_incomes = 0
    for income in incomes:
        sum_incomes += income

    avg = sum_incomes / len(incomes)

    cnt = 0
    for income in incomes:
        if income <= avg:
            cnt += 1

    print('#{}'.format(tc), cnt)