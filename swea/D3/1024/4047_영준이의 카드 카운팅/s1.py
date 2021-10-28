import sys
sys.stdin = open('sample_input.txt')


def check_deck(S):
    cards = {
        'S': [], 'D': [], 'H': [], 'C': [],
    }

    for i in range(0, len(S), 3):
        num = S[i + 1] + S[i + 2]
        if num not in cards.get(S[i]):
            cards.get(S[i]).append(num)
        else:
            return 'ERROR'

    results = ['S', 'D', 'H', 'C']
    for i in range(4):
        results[i] = 13 - len(cards[results[i]])

    return results


T = int(input())
for tc in range(1, 1 + T):
    S = input()

    ans = check_deck(S)

    if type(ans) == str:
        print('#{}'.format(tc), ans)
    else:
        print('#{}'.format(tc), *ans)
