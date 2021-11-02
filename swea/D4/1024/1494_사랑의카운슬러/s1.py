import sys
sys.stdin = open('input.txt')




T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    coords = [list(map(int, input().split())) for _ in range(N)]
