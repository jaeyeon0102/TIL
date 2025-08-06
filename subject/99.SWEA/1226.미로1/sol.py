import sys

sys.stdin = open('input.txt')


def dfs(x,y):
    global check
    if grid[x][y] == '3':
        check = 1
        return 
    
    visited[x][y] = True
    
    for i in range(4):
        dx , dy = x + pos[i][0], y + pos[i][1]
        if 0<= dx < 16 and 0 <= dy < 16 and not visited[dx][dy]:
            visited[dx][dy] =True
            if grid[dx][dy] != '1':
                dfs(dx,dy)
            


for test_case in range(1,11):
    N = int(input())

    grid = [list(input().strip()) for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]
    # 1은 벽, 0은 길, 2는 출발점, 3은 도착점
    pos = [(-1,0),(1,0),(0,1),(0,-1)]


    flag = 0
    check = 0
    for i in range(0,16):
        for j in range(0,16):
            if grid[i][j] == '2':
                visited[i][j] = True
                dfs(i,j)
                flag = 1
                break
        if flag:
            break
    
    print(f"#{test_case} {check}")