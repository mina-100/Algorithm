import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    string = ''
    for _ in range(N):
        alpha, number = input().split()
        string += alpha * int(number)

    print('#{}'.format(tc))
    for i in range(len(string) // 10):
        print(string[10 * i:10 * (i + 1)])
    if len(string) % 10:
        print(string[10 * (len(string) // 10):])

