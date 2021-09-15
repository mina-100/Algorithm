import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    h1, m1, h2, m2 = map(int, input().split())

    # 시간 검사
    if h1 + h2 > 12:
        h_sum = h1 + h2 - 12
    else:
        h_sum = h1 + h2
    # 분 검사
    if m1 + m2 >= 60:
        m_sum = m1 + m2 - 60
        h_sum += 1
    else:
        m_sum = m1 + m2

    print('#{} {} {}'.format(tc, h_sum, m_sum))

