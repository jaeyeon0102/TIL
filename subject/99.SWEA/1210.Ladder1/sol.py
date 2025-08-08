import sys

sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())

    matrix = [list(map(int,input().split())) for _ in range(100)]

    for r in range(100):
        for c in range(100):
            if matrix[r][c] == 2:
                row, col = r,c

    while row >0 :
        matrix[row][col] = 0

        if col > 0 and matrix[row][col-1] == 1:
            col -= 1

        elif col < 99 and matrix[row][col+1] == 1:
            col += 1
        else:
            row -= 1

    print(f"#{test_case} {col}")