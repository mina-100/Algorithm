import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    word = input()
    mirror = {
        'b' : 'd',
        'd' : 'b',
        'p' : 'q',
        'q' : 'p'
    }

    mirror_word = ''
    for i in range(len(word)-1, -1, -1):
        mirror_word += mirror[word[i]]

    print('#{}'.format(tc), mirror_word)
