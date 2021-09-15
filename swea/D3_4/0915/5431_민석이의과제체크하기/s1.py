import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    array = list(map(int, input().split()))

    # 과제 한 학생 체크하기기
   homework = [0] * (N + 1)
    for arr in array:
        homework[arr] = 1

    print('#{}'.format(tc), end=' ')
    for i in range(1, N + 1):
        if homework[i] == 0:
            print(i, end=' ')
    print()
