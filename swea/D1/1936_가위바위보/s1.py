import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())

if A - B == 1 or A - B == -2:
    win = 'A'
else:
    win = 'B'

print(win)


