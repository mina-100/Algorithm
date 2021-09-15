import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, 1 + T):
    a, b = map(int, input().split())
    print('#{} {} {}'.format(test_case, a // b, a % b))

