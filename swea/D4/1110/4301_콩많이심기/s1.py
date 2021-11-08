import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input())

    visited = [[-1] * N for _ in range(M)]
