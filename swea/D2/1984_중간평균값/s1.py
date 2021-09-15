import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    numbers = list(map(int, input().split()))

    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    min_value = numbers[0]
    max_value = numbers[-1]
    sum_mid = 0
    cnt = 0
    for i in range(1, len(numbers)-1):
        # 최소 수 혹은 최대 수가 여러개일 경우 걸러내기
        if numbers[i] != min_value and numbers[i] != max_value:
            sum_mid += numbers[i]
            cnt += 1

    print(numbers)
    print(sum_mid, cnt, len(numbers))
    print('#{}'.format(tc), round(sum_mid / cnt))
