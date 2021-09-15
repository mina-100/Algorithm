import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    # L 이상 U 이하 운동 필요, 실제 진행: X
    L, U, X = map(int, input().split())

    if X > U:
        print('#{}'.format(tc), -1)
    elif X < L:
        print('#{}'.format(tc), L - X)
    else:
        print('#{}'.format(tc), 0)
