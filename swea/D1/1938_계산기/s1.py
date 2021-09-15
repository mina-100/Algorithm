import sys
sys.stdin = open('input.txt')


def calculate(a, b):
    return a + b, a - b, a * b, a // b


a, b = map(int, input().split())
print(*calculate(a, b), sep = '\n')

