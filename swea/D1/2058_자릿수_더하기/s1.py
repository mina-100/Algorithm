import sys
sys.stdin = open('input.txt')

number = int(input())

sum = 0
while number >= 1:
    sum += number % 10
    number = number // 10

print(sum)
