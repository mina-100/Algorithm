import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    strings = input()
    L = len(strings)
    N = int(input())
    numbers = map(int, input().split())

    positions = [0] * (L + 1)
    for number in numbers:
        positions[number] += 1

    result = ''
    for i in range(L):
        result += positions[i] * '-' + strings[i]
    result += positions[-1] * '-'

    print('#{}'.format(tc), result)
