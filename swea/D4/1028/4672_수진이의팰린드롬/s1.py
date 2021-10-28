from itertools import permutations
import sys
sys.stdin = open('sample_input.txt')


def is_pall(x):
    mid = len(x) // 2
    for i in range(mid):
        if x[i] != x[-i - 1]:
            return False
    return True


T = int(input())
for tc in range(1, 1 + T):
    words = input()
    N = len(words)
    numbers = list(range(N))

    pers = list(permutations(numbers, N))

    # 단어 재배열
    strings = set()
    for per in pers:
        tmp = ''
        for num in per:
            tmp += words[num]
        strings.add(tmp)

    max_cnt = 0
    for string in strings:
        cnt = 0
        # 길이 m인 문자열 만들기
        for m in range(2, N + 1):
            for n in range(N - m + 1):
                check = string[n: n + m]
                if is_pall(check):
                    cnt += 1
        max_cnt = max(max_cnt, cnt)

    print('#{}'.format(tc), max_cnt + N)



