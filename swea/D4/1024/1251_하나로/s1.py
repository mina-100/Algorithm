import sys
sys.stdin = open('input.txt')


def tax(e, maxV, X, Y):
    key = [maxV] * N
    key[0] = 0
    visited = [False] * N

    for _ in range(N):
        start = -1
        minV = maxV
        for i in range(N):
            if not visited[i] and key[i] < minV:
                minV = key[i]
                start = i

        visited[start] = True
        for end in range(N):
            if not visited[end]:
                distance = (X[start] - X[end]) ** 2 + (Y[start] - Y[end]) ** 2
                if key[end] > distance:
                    key[end] = distance
    return round(sum(key) * e)


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    coordX = list(map(int, input().split()))
    coordY = list(map(int, input().split()))
    E = float(input())

    limitV = N * 1000000 ** 2 * 2
    print('#{}'.format(tc), tax(E, limitV, coordX, coordY))
