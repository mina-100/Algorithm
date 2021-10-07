import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    a = input()

    strings = sorted(a)
    stack = []
    for string in strings:
        if not stack or stack[-1] != string:
            stack.append(string)
        else:
            if stack[-1] == string:
                stack.pop()

    if not stack:
        print('#{}'.format(tc), 'Good')
    else:
        remain = ''.join(stack)
        print('#{}'.format(tc), remain)
