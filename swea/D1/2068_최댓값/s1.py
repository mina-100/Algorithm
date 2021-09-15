import sys
sys.stdin = open('input.txt')

# 입력 받기
T = int(input())
for test_case in range(1, 1+T):
    number_list = list(map(int, input().split()))

    # 가장 큰 값 제일 뒤로 보내기
    for i in range(len(number_list) - 1):
        if number_list[i] > number_list[i+1]:
            number_list[i], number_list[i+1] = number_list[i+1], number_list[i]

    print('#{} {}'.format(test_case, number_list[-1]))

