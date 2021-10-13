import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    loads = [0] * N
    for i in range(N):
        loads[i] = int(input())

    avg = sum(loads) // N
    cnt = 0
    for load in loads:
        if load < avg:
            cnt += (avg - load)

    print('#{}'.format(tc), cnt)
