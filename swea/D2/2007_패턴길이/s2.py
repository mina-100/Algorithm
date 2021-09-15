import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, 1 + T):
    string = input()
    ptn_len_max = 10    # 패턴 마디의 최대 길이

    # 패턴 길이를 담을 리스트 선언
    ptn_list = []
    # 인덱스를 패턴 마디의 길이로 하여, 역순으로 탐색
    for i in range(1, ptn_len_max + 1):
        # 패턴 확인 후, 일치할 경우 count_list 에 인덱스 추가
        if string[:i] == string[i:i + i]:
            ptn_list.append(string[:i])
    # 패턴 길이가 여러개일경우 - 패턴단어 내 반복이 있거나, 패턴 여러개가 1개로 인식된 경우 발생 가능
    if len(ptn_list) > 1:
        for j in range(len(ptn_list) - 1):
            result = ptn_list[-1]
            # 가장 긴 길이와 배수관계가 아닐 경우, 더 긴 길이가 패턴 ex) ababc
            if len(result) % len(ptn_list[j]):
                continue
            # 배수 관계일 경우, 패턴 내 반복된 단어인지, 패턴의 중복인지 확인 필요 ex) ababcd
            else:
                if ptn_list[j] * (len(result) // len(ptn_list[j])) == result:
                    result = ptn_list[j]
                    break
    else:
        result = ptn_list[0]
    print('#{}'.format(test_case), len(result))
