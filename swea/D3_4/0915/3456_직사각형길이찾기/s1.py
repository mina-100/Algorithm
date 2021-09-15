import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    lengths = list(map(int, input().split()))

    lengths.sort()
    # count 결과가 홀수: 짧은 길이가 1개 or 3개(정사각형)
    if lengths.count(lengths[0]) % 2:
        print('#{}'.format(tc), lengths[0])
    else:
        print('#{}'.format(tc), lengths[-1])