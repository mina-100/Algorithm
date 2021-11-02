N = 1000000
decimals = [True] * (N + 1)

decimals[2] = 2

for i in range(2, N + 1):
    # True 이면 소수
    if decimals[i]:
        decimals[i] = i
        print(i, end=' ')
        for j in range(1, (N // i) + 1):
            decimals[i * j] = False
