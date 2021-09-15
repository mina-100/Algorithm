import sys
sys.stdin = open('input.txt')

N = int(input())

for number in range(N, -1, -1):
    print(number, end = ' ')