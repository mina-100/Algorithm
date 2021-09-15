import sys
sys.stdin = open('input.txt')


N = int(input())

if N > 99:
    cnt = 99
    for number in range(100, N + 1):
        num1 = number % 10
        num2 = (number // 10) % 10
        num3 = (number // 10) // 10
        if num2 - num1 == num3 - num2:
            cnt += 1
    print(cnt)
else:
    print(N)
