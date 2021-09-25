import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    scores = [0] * N

    for b in B:
        for idx, a in enumerate(A):
            if b < a:
                continue
            else:
                scores[idx] += 1
                break

    max_score = max(scores)
    for i, score in enumerate(scores):
        if score == max_score:
            result = i + 1
            break

    print('#{}'.format(tc), result)

