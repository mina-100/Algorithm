import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, 1 + T):
    a, b = map(int, input().split())
    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    else:
        result = '='
    print('#{} {}'.format(test_case, result))

