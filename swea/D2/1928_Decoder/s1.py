import sys
sys.stdin = open('input.txt')


def decording(strings):
    # 인덱스값 받아오는 반복문 돌리기
    # 결과값 이진수로 변환 후 저장
    result = ''
    for string in strings:
        for idx, char in enumerate(decorder_list):
            if string == char:
                bin_number = str(format(idx, 'b'))
                while len(bin_number) < 6:
                    bin_number = '0' + bin_number
                result += bin_number
    return result


def encoding(numbers):
    answer = ''
    for i in range((len(numbers) // 8) - 1):
        num = int(numbers[8 * i:8 * (i + 1)], 2)
        answer += chr(num)
    return answer


T = int(input())
for tc in range(1, 1 + T):
    strings = input()

    decorder_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
                     ]

    print('#{} {}{}'.format(tc, encoding(decording(strings)), '.'))





