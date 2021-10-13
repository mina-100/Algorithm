import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    words = input()

    def half(strings):
        check = set()
        for string in strings:
            check.add(string)
        if len(check) == 2:
            return 'Yes'
        return 'No'

    print('#{}'.format(tc), half(words))