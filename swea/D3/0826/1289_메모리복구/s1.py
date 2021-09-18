import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    memories = input()

    # 메모리에서 1의 처음 위치를 시작점으로 설정
    start = memories.find('1')
    stack = ['1']
    # 시작점이 메모리의 끝이 아닐 경우
    if start != len(memories) - 1:
        for i in range(start + 1, len(memories)):
            # stack 의 top 과 다른 문자열을 만나면 stack 에 push
            if memories[i] != stack[-1]:
                stack.append(memories[i])

    print('#{}'.format(tc), len(stack))