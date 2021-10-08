import sys
sys.stdin = open('input.txt')


def how_long(l, r):
    while l != r:
        mid = (l + r) // 2
        balloon = 0
        for i in range(N):
            balloon += mid // times[i]
        if balloon >= M:
            r = mid
        elif balloon <= M:
            l = mid + 1
    return l


N, M = map(int, input().split())
times = list(map(int, input().split()))
min_t = min(times)
max_t = max(times) * M

print(how_long(min_t, max_t))
