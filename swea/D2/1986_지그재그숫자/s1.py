import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    number = int(input())

    if number % 2:
        sum = (-1) * (number // 2) + number
    else:
        sum = (-1) * (number // 2)

    print('#{} {}'.format(tc, sum))

