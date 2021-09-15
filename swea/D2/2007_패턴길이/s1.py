import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, 1 + T):
    string = input()
    # 패턴의 최대 길이
    ptn_len_max = 10

    count_ptn = []
    for i in range(ptn_len_max, 0, -1):
        if string[0:i] == string[i:i + i]:
            count_ptn.append(i)
    # 검사 진행
    if len(count_ptn) > 1:
        for j in range(len(count_ptn) - 1):
            if count_ptn[j] % count_ptn[j + 1]:
                result = count_ptn[j]
            else:
                result = count_ptn[j + 1]
    else:
        result = count_ptn[0]
    print('#{}'.format(test_case), result)
