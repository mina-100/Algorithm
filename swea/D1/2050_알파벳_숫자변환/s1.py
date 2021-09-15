import sys
sys.stdin = open('input.txt')

words = input()

words_to_num = []
for i in range(len(words)):
    capital_word = words.upper()
    words_to_num.append(ord(capital_word[i])-64)

print(*words_to_num)


