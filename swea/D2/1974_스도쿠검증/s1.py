import sys
sys.stdin = open('input.txt')


# 행/열 검사
def is_sudoku_1(matrix, N):
    for i in range(N):
        check_set = set()
        for j in range(N):
            check_set.add(matrix[i][j])
        if len(check_set) != 9:
            return False
            break
    return True


# 3 * 3 검사
def is_sudoku_2(matrix, N):
    for n in range(1, 4):
        for m in range(1, 4):
            check_set = set()
            for i in range(3 * (n - 1), 3 * n):
                for j in range(3 * (m - 1), 3 * m):
                    check_set.add(matrix[i][j])
            if len(check_set) != 9:
                return False
                break
    return True


T = int(input())
for tc in range(1, 1 + T):
    N = 9
    sudoku = [list(map(int, input().split())) for _ in range(N)]
    reverse_sudoku = list(map(list, zip(*sudoku)))

    if is_sudoku_1(sudoku, N) == True and is_sudoku_1(reverse_sudoku, N) == True and is_sudoku_2(sudoku, N) == True:
        print('#{}'.format(tc), 1)
    else:
        print('#{}'.format(tc), 0)


