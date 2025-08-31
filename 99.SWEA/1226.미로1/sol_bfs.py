import sys

sys.stdin = open('input.txt')

from collections import deque

def bfs(x,y):

    queue = deque()
    queue.append((x,y))
    

    while queue:
        row, col = queue.popleft()
        
        
        for i in range(4):
            dx, dy = row + pos[i][0] , col + pos[i][1]
            if dx < 0 or dx >= 16 or dy < 0 or dy >= 16:
                continue
            
            if visited[dx][dy]:
                continue

            if grid[dx][dy] == '1':
                continue

            if grid[dx][dy] == '3':
                return 1
            
            visited[dx][dy] = True
            queue.append((dx,dy))
            
    return 0

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
                print(f"#{test_case} {bfs(i,j)}")
                flag = 1
                break
        if flag:
            break

    