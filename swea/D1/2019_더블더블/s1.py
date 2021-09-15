import sys
sys.stdin = open('input.txt')

number = int(input())
for i in range(number + 1):
    print(2 ** i, end=' ')

