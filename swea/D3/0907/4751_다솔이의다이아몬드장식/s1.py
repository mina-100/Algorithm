import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    strings = input()
    n = len(strings)
    word_1 = '..#.' * n + '.'
    word_2 = '.#.#' * n + '.'

    word_3 = ''
    for string in strings:
        word_3 += '#.' + string + '.'

    print(word_1)
    print(word_2)
    print('{}#'.format(word_3))
    print(word_2)
    print(word_1)
