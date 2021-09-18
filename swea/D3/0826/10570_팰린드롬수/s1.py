import sys
sys.stdin = open('input.txt')


def is_palindrome(numbers):
    pallin_list = []
    for number in numbers:
        # 회문 검사
        if number == number[::-1]:
            pallin_list.append(number)
    return pallin_list


T = int(input())
for tc in range(1, 1 + T):
    A, B = map(int, input().split())
    numbers = list(map(str, range(A, B + 1)))

    root_numbers = []
    for num in is_palindrome(numbers):
        # 제곱근이 정수인지 검사
        root_num = int(num) ** (1/2)
        if root_num == int(root_num):
            root_numbers.append(str(int(root_num)))

    print('#{}'.format(tc), len(is_palindrome(root_numbers)))
