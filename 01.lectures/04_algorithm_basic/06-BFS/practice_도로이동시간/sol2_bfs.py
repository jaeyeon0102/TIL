import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def get_road_move_time(road, N, M):
    queue = deque()
    queue.append((0,0,0))
    visited = [0*M for _ in range(N)]
    visited[0][0] = 1

    while queue:
        row , col , dist = queue.popleft()

        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visited[nx][ny]:
                continue

            if road[nx][ny] == 0:
                continue

            if nx == N -1 and ny == M-1:
                return dist + 1 #지금까지 도달한 거리 + 1 해서 반환
            
            # 위 조건을 모두 통과하고 여기까지 왔다?
            visited[nx][ny] =1
            queue.append((nx,ny,dist+1))
    return -1

# 도로의 크기 N * M 입력 받기
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]
result = get_road_move_time(road, N, M)
print(result)
