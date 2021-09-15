import sys
sys.stdin = open('input.txt')

N = int(input())
number_list = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    for j in range(0, i):
        if number_list[j] > number_list[j + 1]:
            number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
mid_num = number_list[N//2]

print(mid_num)

