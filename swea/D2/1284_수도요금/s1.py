import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    '''
    P: A사 리터당 요금
    Q: B사 R리터 이하 기본 요금
    S: B사 R리터 이상 리터당 요금
    W: 수도 사용량
    '''
    P, Q, R, S, W = map(int, input().split())

    cost_A = W * P
    if W > R:
        cost_B = Q + S * (W - R)
    else:
        cost_B = Q

    if cost_A > cost_B:
        print('#{}'.format(tc), cost_B)
    else:
        print('#{}'.format(tc), cost_A)

