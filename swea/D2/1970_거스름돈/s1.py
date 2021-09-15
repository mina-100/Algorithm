import sys
sys.stdin = open('input.txt')


def changes(N):
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_cnt = [0] * len(moneys)
    for i in range(len(moneys)):
        if N // moneys[i] > 0:
            money_cnt[i] = N // moneys[i]
            N = N % moneys[i]
    return money_cnt


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    print('#{}'.format(tc))
    print(*changes(N))


