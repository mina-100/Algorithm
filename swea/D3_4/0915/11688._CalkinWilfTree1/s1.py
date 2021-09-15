import sys
sys.stdin = open('sample_input.txt')


def calkin_wilf(strings):
    a = b = 1
    for string in strings:
        if string == 'L':
            b = a + b
        else:
            a = a + b
    return a, b


T = int(input())
for tc in range(1, 1 + T):
    strings = input()
    (a, b) = calkin_wilf(strings)

    print('#{}'.format(tc), a, b)
