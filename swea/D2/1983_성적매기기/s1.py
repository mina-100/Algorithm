import sys
sys.stdin = open('input.txt')


def ranking(rank):
    n = N // 10
    standard = {'A+': list(range(0, n)), 'A0': list(range(n, 2 * n)), 'A-': list(range(2 * n, 3 * n)),
                'B+': list(range(3 * n, 4 * n)), 'B0': list(range(4 * n, 5 * n)), 'B-': list(range(5 * n, 6 * n)),
                'C+': list(range(6 * n, 7 * n)), 'C0':list(range(7 * n, 8 * n)), 'C-':list(range(8 * n, 9 * n)),
                'D0': list(range(9 * n, 10 * n)),
                }
    for key, value in standard.items():
        if rank in value:
            return key


T = int(input())
for tc in range(1, 1 + T):
    N, K = map(int, input().split())

    # 점수 계산하기
    scores = []
    for _ in range(N):
        mid, fin, hw = map(int, input().split())
        score = mid * 0.35 + fin * 0.45 + hw * 0.2
        scores.append(score)

    # 점수 내림차순 정렬하여 등수 찾기
    final_score = sorted(scores, reverse=True)
    for i in range(N):
        if scores[K - 1] == final_score[i]:
            rank = i

    print('#{}'.format(tc), ranking(rank))

