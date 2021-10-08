import sys
sys.stdin = open('sample_input.txt')


def immigration(l, r):
    while l != r:
        mid_time = (l + r) // 2
        people = M
        for t in times:
            # 입국심사 통과 가능한 사람의 수
            people -= mid_time // t
        # 시간 과다
        if people <= 0:
            r = mid_time
        # 시간 부족
        elif people >= 0:
            l = mid_time + 1
    return l


T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    times = [int(input()) for _ in range(N)]
    min_t = min(times)
    max_t = min(times) * M

    print('#{}'.format(tc), immigration(min_t, max_t))
