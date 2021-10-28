import sys
sys.stdin = open('sample_input.txt')


def frog(cryings):
    global min_frog
    cry_frogs = ['c', 'r', 'o', 'a', 'k']
    count_frogs = [0] * 5

    # 울음소리 카운트하기
    for crying in cryings:
        for idx, val in enumerate(cry_frogs):
            if crying == val:
                count_frogs[idx] += 1
                # 다음 울음이 먼저 진행되면 불가능
                if idx != 0 and count_frogs[idx] > count_frogs[idx - 1]:
                    min_frog = -1
                    return
                break

        # 마지막 울음이 들리면
        if count_frogs[-1]:
            # 최소 개구리 수 업데이트
            min_frog = max(min_frog, count_frogs[0])
            # 끝까지 다 울 수 있는지?
            for i in range(5):
                count_frogs[i] -= 1

    # 남는 울음이 있는지 체크
    for j in range(5):
        if count_frogs[j] != 0:
            min_frog = -1
            return


T = int(input())
for tc in range(1, 1 + T):
    cryings = input()
    min_frog = 0
    frog(cryings)

    print('#{}'.format(tc), min_frog)




