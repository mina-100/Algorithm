import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, 1 + T):
    number_list = list(map(int, input().split()))

    sum_number = 0
    cnt = 0
    for i in range(len(number_list)):
        sum_number += number_list[i]
        cnt += 1
    avg = round(sum_number / cnt)
    print('#{} {}'.format(test_case, avg))
