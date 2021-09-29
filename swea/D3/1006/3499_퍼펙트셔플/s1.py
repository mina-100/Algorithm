import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    cards = list(input().split())
    num = len(cards)
    mid_num = num // 2

    if num % 2:
        deck_1 = cards[:mid_num + 1]
        deck_2 = cards[mid_num + 1:]
    else:
        deck_1 = cards[:mid_num]
        deck_2 = cards[mid_num:]

    print('#{}'.format(tc), end=' ')
    for i in range(mid_num):
        print(deck_1[i], end=' ')
        print(deck_2[i], end=' ')
    if num % 2:
        print(deck_1[-1], end=' ')
    print()
