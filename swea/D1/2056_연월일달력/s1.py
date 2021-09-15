import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, 1 + T):
    date = input()

    year = date[:4]
    month = date[4:6]
    day = date[6:8]

    month_30_list = ['04', '06', '09', '11']
    if int(day) < 1 or int(day) > 31 or not int(month) in range(1, 13):
        result = -1
    elif month == '02' and int(day) > 28:
        result = -1
    elif month in month_30_list and int(day) > 30:
        result = -1
    else:
        result = year + '/' + month + '/' + day

    print('#{}'.format(test_case), result)

