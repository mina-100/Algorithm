import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    number = int(input())

    num_set = set()
    a = 0
    while len(num_set) < 10:
        a += 1
        N = a * number
        if N < 10:
            num_set.add(N)
        else:
            while N > 0:
                num_set.add(N % 10)
                N = N // 10

    print('#{} {}'.format(tc, a * number))

