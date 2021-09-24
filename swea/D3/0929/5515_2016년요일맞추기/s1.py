import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    m, d = map(int, input().split())

    # 2016.01.01: 금요일(4), 2016년: 윤년
    first = 4
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 1월 1일부터 몇일 뒤인지 구하기
    # 직전달 까지의 날짜의 합 + 이번달 날짜 - (1월 1일)
    number = d - 1
    for i in range(1, m):
        number += days[i]

    add = number % 7

    if first + add > 6:
        print('#{}'.format(tc), first + add - 7)
    else:
        print('#{}'.format(tc), first + add)
