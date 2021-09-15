import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, 1 + T):
    number_list = list(map(int, input().split()))

    odd_sum = 0
    for i in range(len(number_list)):
        if number_list[i] % 2:
            odd_sum += number_list[i]

    print('#{} {}'.format(test_case, odd_sum))


