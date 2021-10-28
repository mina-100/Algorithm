import sys
sys.stdin = open('sample_input.txt')


def is_valid(N):
    numbers = list(range(1, 10))
    if N > 81:
        return 'No'
    for number in numbers:
        if not N % number and N // number < 10:
            return 'Yes'
    return 'No'


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    print('#{}'.format(tc), is_valid(N))
