import sys
sys.stdin = open('input.txt')


def is_palindrome(strings):
    for i in range(len(strings) // 2):
        if strings[i] != strings[-i-1]:
            return 0
        else:
            return 1


T = int(input())
for tc in range(1, 1 + T):
    strings = input()

    print('#{} {}'.format(tc, is_palindrome(strings)))

