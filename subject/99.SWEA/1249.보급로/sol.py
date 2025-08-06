import sys
sys.stdin = open('input.txt')

from collections import deque

pos = [(-1,0),(1,0),(0,1),(0,-1)]

def bfs(map, N):
    dist = [[float('inf')] * N for _ in range(N)]
    visited = [([False] * N) for _ in range(N)]
    queue = deque()
    dist[0][0] = 0
    queue.append((0,0))
    visited[0][0] = True

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx, dy = x + pos[i][0] , y + pos[i][1]
            
            if 0 <= dx < N and 0 <= dy < N:
                new_cost = dist[x][y] + int(map[dx][dy])
                if new_cost < dist[dx][dy]:
                    dist[dx][dy] = new_cost
                    queue.append((dx,dy))
            
            # print(dist)
        
    return dist[N-1][N-1]
            


T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    matrix = [list(input().strip()) for _ in range(N)]

    print(f"#{test_case} {bfs(matrix,N)}")