import sys
sys.stdin = open('input.txt')


# 빈 칸 길이 검사하는 함수 선언
def how_long(N, K, NxN):
    count_list = [0] * (N + 1)
    for i in range(N):
        cnt = 0
        for j in range(N):
            if NxN[i][j] == 1:
                    cnt += 1
                    if j == N - 1:
                        count_list[cnt] += 1
            else:
                count_list[cnt] += 1
                cnt = 0
    return count_list[K]


T = int(input())
for test_case in range(1, 1 + T):
    N, K = map(int, input().split())
    NxN = [list(map(int, input().split())) for _ in range(N)]

    # 가로 결과
    result_row = how_long(N, K, NxN)

    # 세로 결과
    reverse_NxN = list(map(list, zip(*NxN)))
    result_col = how_long(N, K, reverse_NxN)

    print('#{}'.format(test_case), result_row + result_col)



