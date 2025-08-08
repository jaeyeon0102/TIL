import sys

sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1,T+1):
    N = int(input())
    cnt = 0
    box = [[0]*10 for _ in range(10)]
    for _ in range(N):
        matrix = list(map(int, input().split()))
        for i in range(matrix[0],matrix[2]+1):
            for j in range(matrix[1],matrix[3]+1):
                if box[i][j] == 0:
                    box[i][j] = matrix[4]
                elif box[i][j] == -1:
                    continue
                elif box[i][j] != matrix[4]:
                    box[i][j] = -1
                    cnt += 1


    print(f"#{test_case} {cnt}")