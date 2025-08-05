import sys

sys.stdin = open('input.txt')


def dfs(x,y,k):
    global result

    visited[x][y] = True
    result += 1    
    dx , dy = x + pos[k][0] , y + pos[k][1]
    
    if (0<= dx < N and 0<= dy <M) and not visited[dx][dy] and grid[dx][dy] == 1:
        dfs(dx, dy,k)
    return result
    
T = int(input())

for test_case in range(1,T+1):
    N,M = map(int, input().split())

    grid = [list(map(int,input().split())) for _ in range(N)]
    
    pos = [(-1,0),(1,0),(0,1),(0,-1)]

    max_length = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                for k in range(4):
                    visited = [([False] * M) for _ in range(N)]
                    result = 0
                    dfs(i,j,k)
                    max_length = max(max_length,result)
    
    print(f"#{test_case} {max_length}")