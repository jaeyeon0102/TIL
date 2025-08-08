import sys

sys.stdin = open('input.txt')


def dfs(row, cost):
    # 최소 비용
    global min_cost

    # 가지치기
    if cost >= min_cost:
        return
        

    # 결과값 도출 -> 열을 모두 순회했을 때
    if row == N:
        min_cost = min(cost,min_cost)
        return
    
    
    # 행마다 순회
    for col in range(1,N):
        # 방문을 안했고, col과 row가 동일하지 않을 때
        if (not visited[col]) and (col != row):
            # 방문
            visited[col] = True
            dfs(row+1, cost + board[row][col])
            # 백트래킹
            visited[col] = False

# 입력
T = int(input())

for test_case in range(1,T+1):
    # 크기 입력 
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    # 열마다 방문 여부 
    visited = [False] * N
    
    # 3 <= N <= 10 이고, 100이하의 자연수 -> 100 * 10* 10 = 1000
    min_cost = 10001

    # dfs (시작 열, cost)
    dfs(0,0)

    # 출력
    print(f"#{test_case} {min_cost}")