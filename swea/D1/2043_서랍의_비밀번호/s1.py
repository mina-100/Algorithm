import sys
sys.stdin = open('input.txt')

password, start = map(int, input().split())

if password - start > 0:
    print(password - start +1)
else:
    print('비밀번호를 찾을 수 없습니다.')

