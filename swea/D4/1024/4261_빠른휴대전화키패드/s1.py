import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    S, N = input().split()
    words = list(input().split())

    keypads = ['0', '0', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    cnt = 0
    for word in words:
        tmp = ''
        for w in word:
            for idx, keypad in enumerate(keypads):
                if w in keypad:
                    tmp += str(idx)
                    break

        if tmp == S:
            cnt += 1

    print('#{}'.format(tc), cnt)