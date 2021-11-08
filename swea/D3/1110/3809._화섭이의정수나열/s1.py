import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    numbers = list(map(int, input().split()))
