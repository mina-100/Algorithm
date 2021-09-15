import sys
sys.stdin = open('input.txt')

number = int(input())

sum = 0
for num in range(number + 1):
    sum += num

print(sum)