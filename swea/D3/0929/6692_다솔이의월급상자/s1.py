import sys
sys.stdin = open('S_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    sum_salary = 0
    for _ in range(N):
        p, salary = map(float, input().split())
        sum_salary += p * salary
    print('#{} {:6f}'.format(tc, sum_salary))
