import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    arr = list(input().split())
    N = int(arr.pop(0))

    past_color = arr[0]
    past_org = past_bl = 1
    time = 0
    tmp_time = 0
    for i in range(N):
        now_color, now = arr[2 * i], int(arr[2 * i + 1])

        if now_color == past_color:
            if now_color == 'O':
                time += abs(now - past_org)
                past_org = now
            else:
                time += abs(now - past_bl)
                past_bl = now
        else:
            if now_color == 'O':
                if now > past_bl:
                    time += abs(now - past_bl)
                    past_org = now
                else:
                    time += 1
                    past_org = now
            else:
                if now > past_org:
                    time += abs(now - past_org)
                    past_bl = now
                else:
                    time += 1
                    past_bl = now
        past_color = now_color

    print(time)
