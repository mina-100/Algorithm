import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    strings = input()

    vowel = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for string in strings:
        if string in vowel:
            continue
        else:
            result += string
    print('#{}'.format(tc), result)
