import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    now, later = map(int, input().split())
    time = now + later

    if time >= 24:
        print('#{}'.format(tc), time - 24)
    else:
        print('#{}'.format(tc), time)

