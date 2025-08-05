# 실패

def dfs(x,y,dx,dy):
    if not (0<=x <M and 0<= y < N):
        return 0
    if visited[x][y] or grid[x][y] == 0:
        return 0
    
    visited[x][y] = 1

    return 1 + dfs(x + dx, y + dy, dx, dy)

T = int(input())

for test_case in range(1,T+1):
    N,M = map(int, input().split())

    grid = [list(map(int,input().split())) for _ in range(M)]
    
    pos = [(1,0),(0,1)]

    max_length = 0

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                for x,y in pos:
                    visited = [([0] * N) for _ in range(M)]
                    result = dfs(i,j,x,y)
                    max_length = max(max_length,result)
    
    print(f"#{test_case} {max_length}")