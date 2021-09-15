import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 수
T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())    # 커맨드의 수
    command_list = [list(map(int, input().split())) for _ in range(N)]
    v = 0   # 속도
    distance = 0    # 이동거리
    for idx in range(N):
        # command_list[idx]의 길이가 1일 경우, 현재 속도 유지이므로 가속도값 없음
        if len(command_list[idx]) != 1:
            # command_list[idx][0]: 가속도 방향, command_list[idx][-1]: 가속도 값 의미
            # 가속도가 양수일 경우
            if command_list[idx][0] == 1:
                # 이전 속도에 가속도 더하기
                v += command_list[idx][1]
            # 가속도가 음수일 경우, 이전 속도에 가속도를 뺀 값이 0 이하일 경우 속도를 0으로 초기화한다.
            elif v - command_list[idx][1] > 0:
                v -= command_list[idx][1]
            else:
                v = 0
        # 각 속도로 1초씩 이동하므로, 이동거리에 v 씩 더해준다.
        distance += v

    print('#{} {}'.format(test_case, distance))

