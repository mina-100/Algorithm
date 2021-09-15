import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 버블정렬
    for i in range(N, 1, -1):
        for j in range(i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print('#{}'.format(tc), *numbers)

