import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    if N % 2:
        print('#{}'.format(tc), 'Odd')
    else:
        print('#{}'.format(tc), 'Even')
