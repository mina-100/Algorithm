import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, 1 + T):
    A, B = input().split()

    # 두 수중 하나라도 10 이상일 경우
    if len(A) > 1 or len(B) > 1:
        print('#{}'.format(tc), -1)
    else:
        print('#{}'.format(tc), int(A) * int(B))


# 조금 더 느림

# T = int(input())
# for tc in range(1, 1 + T):
#     A, B = map(int, input().split())
#
#     # 두 수중 하나라도 10 이상일 경우
#     if A // 10 > 0 or B // 10 > 0:
#         print('#{}'.format(tc), -1)
#     else:
#         print('#{}'.format(tc), A * B)

