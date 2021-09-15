import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 수
T = int(input())
for test_case in range(1, 1+ T):
    mon1, day1, mon2, day2 = map(int, input().split())

    day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 누적합 리스트 및 누적합 변수 선언
    day_sum_list = [0]
    day_sum = 0
    for i in range(1, len(day_list)):
        day_sum += day_list[i]
        day_sum_list.append(day_sum)
        # [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        # ex. day_sum_list[7] - day_sum_list[5] ==> 6, 7 월 모든 날짜 포함
    d_day = day_sum_list[mon2-1] - day_sum_list[mon1-1] - (day1 - 1) + day2
    print('#{} {}'.format(test_case, d_day))
