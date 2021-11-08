import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    happy_days = [int(input()) for _ in range(N)]
    gaps = [happy_days[1] - 1]
    for i in range(2, N):
        flag = 1
        check = happy_days[i] - 1
        for gap in gaps:
            if not check % gap:
                flag = 0
                break
        if flag:
            gaps.append(check)

    print('#{}'.format(tc), len(gaps))
