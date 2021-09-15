import sys
sys.stdin = open('input.txt')

N = int(input())

divisor_list = []
for divisor in range(1, N + 1):
    if not N % divisor:
        divisor_list.append(divisor)

print(*divisor_list)
