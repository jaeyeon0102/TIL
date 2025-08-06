import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def get_road_move_time(row,col):
    # 너비 우선 탐색 -> queue
    # queue = deque([(0,0)])
    queue = deque()

    queue.append((0,0)) # 시작 정점 후보군에 삽입
    distance[0][0] = 0 # 시작 위치까지 이동거리는 0

    # BFS 탐색
    while queue:
        row, col = queue.popleft()
        #이 위치에서 4방향에 대한 탐색
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]
            if 0<= nx < N and 0 <= ny < M and distance[nx][ny] == -1 and data[nx][ny]:
                queue.append((nx,ny))
                distance[nx][ny] = distance[row][col] + 1

                if nx == N -1 and ny == M-1: #도착지라면
                    return 
    # 모든 후보군을 다 탐색했지만, return 된 적 없다면 
    # 도착할 수 없다는 의미
    return -1

# 데이터 입력
# row: N col:M

N,M = map(int, input().split())
data = [list(map(int,input())) for _ in range(N)]

# 방문 표시 -> 우리의 최종 목적은?
# 해당 위치까지 도달하는 데 걸린 비용이 얼만지 기록
distance = [[-1] * M for _ in range(N)]

# print(distance)

get_road_move_time(0,0)

print(distance[N-1][M-1])

for dis in distance:
    print(*dis)