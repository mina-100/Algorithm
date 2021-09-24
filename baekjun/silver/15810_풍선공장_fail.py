import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
times = list(map(int, input().split()))
number = min(times) * M

# 시간초과 코드

# for i in range(number):
#     balloon = 0
#     for time in times:
#         balloon += i // time
#     if balloon == M:
#         print(i)
#         break
#
# balloons = [0] * M * min(times)
# for i in range(1, len(balloons)):
#     balloons[i] = balloons[i - 1]
#     for j in range(N):
#         if i % times[j] == 0:
#             balloons[i] += 1
#     if balloons[i] == M:
#         result = i
#         break

# print(result)
