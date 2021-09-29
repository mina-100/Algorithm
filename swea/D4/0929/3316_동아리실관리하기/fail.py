import sys
sys.stdin = open('sample_input.txt')


def kkk(n):
    memo = [0] * n
    # A(key), 책임자 필참 =>
    possible = 1 * 2 * 2 * 2
    impossible = 9
    if directors[0] != 'A':
        # A(key), 책임자: 필참 => 경우의 수 1
        # 그 외: 참여 or 불참 => 경우의 수 2
        memo[0] = possible // 2
        memo[1] = memo[0] * possible - 3
    else:
        memo[0] = possible
        memo[1] = memo[0] * possible - impossible
    i = 1
    while i < n - 1:
        i += 1
        memo[i] = memo[i - 1] * possible
        # 전날과 오늘 책임자가 다른 경우, 불가능한 케이스 빼기
        if directors[i - 1] != directors[i]:
            memo[i] -= memo[i - 2] * impossible
    return memo[-1]


T = int(input())
for tc in range(1, 1 + T):
    directors = input()
    n = len(directors)
    print(n)
    print(kkk(n))

