import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    prices = list(map(int, input().split()))

    profit = 0      # 수익
    max_price = prices[0]       # 가장 비싼 값
    past_idx = -1
    now_idx = 0     # 가장 비싼 값의 idx
    while past_idx < N - 1:
        price_sum = 0
        for i in range(past_idx + 1, N):
            if prices[i] >= max_price:
                # 최대값 및 idx 재할당
                max_price = prices[i]
                now_idx = i
                if past_idx == now_idx:
                    break
        for j in range(past_idx + 1, now_idx):
            price_sum += prices[j]
        profit += (max_price * (now_idx - past_idx - 1)) - price_sum
        past_idx = now_idx
        max_price = 0

    print('#{}'.format(tc), profit)