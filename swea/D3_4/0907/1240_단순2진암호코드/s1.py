import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    codes = [input() for _ in range(N)]

    trans_code = ['0001101', '0011001', '0010011', '0111101', '0100011',
                  '0110001', '0101111', '0111011', '0110111', '0001011']

    # 암호 변환
    password = ''
    for code in codes:
        if len(password) > 0:
            break
        for i in range(M - 1, -1, -1):
            if code[i] == '1':
                password = code[i - 55:i+1]
                break

    check = []
    for j in range(8):
        x = password[j * 7:(j + 1) * 7]
        check.append(trans_code.index(x))

    # 암호 검사
    check_sum = 0
    for k in range(4):
        check_sum += check[2 * k] * 3 + check[2 * k + 1]

    if check_sum % 10 == 0:
        print('#{}'.format(tc), sum(check))
    else:
        print('#{}'.format(tc), 0)
