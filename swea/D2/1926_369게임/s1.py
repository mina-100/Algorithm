import sys
sys.stdin = open('input.txt')


def game369(n):
    claps = ['3', '6', '9']
    number_list = list(range(1, N + 1))
    for number in number_list:
        cnt = 0
        # str 으로 타입 변경하여 각 자리별로 검사
        for num in str(number):
            if num in claps:
                cnt += 1
                number_list[number-1] = '-' * cnt
    return number_list


N = int(input())

print(*game369(N))


