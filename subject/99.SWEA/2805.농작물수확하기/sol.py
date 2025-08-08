# import sys
#
# sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    matrix = [list(map(int, input())) for _ in range(N)]
    cnt = 0
    start , end = N//2, N//2

    for i in range(N):
        for j in range(start,end+1):
            cnt += matrix[i][j]
        if N//2 > i:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f"#{test_case} {cnt}")
