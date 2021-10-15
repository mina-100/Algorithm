from itertools import combinations
import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    numbers = list(map(int, input().split()))
    combis = list(combinations(numbers, 3))

    sum_lst = set()
    for combi in combis:
        tmp_sum = 0
        for com in combi:
            tmp_sum += com
        sum_lst.add(tmp_sum)
    result = list(sum_lst)
    result.sort(reverse=True)

    print('#{}'.format(tc), result[4])
