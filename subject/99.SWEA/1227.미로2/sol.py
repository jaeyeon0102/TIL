import sys

sys.stdin = open('input.txt')

from collections import deque

def bfs(x,y):

    queue = deque()     # 큐 생성
    queue.append((x,y)) # 시작 지점 좌표 추가
    

    while queue:                    # 큐가 존재할 때
        row, col = queue.popleft()  
        
        for i in range(4): # 상하좌우
            dx, dy = row + pos[i][0] , col + pos[i][1]  # dx,dy : 이동한 좌표
            # 만약 좌표 내에 없다면
            if dx < 0 or dx >= 100 or dy < 0 or dy >= 100:
                continue
            # 이미 방문했다면
            if visited[dx][dy]:
                continue
            # 갈 수 없는 곳이라면
            if grid[dx][dy] == '1':
                continue

            # 정답 구간이라면 return 1
            if grid[dx][dy] == '3':
                return 1
            
            # 모든 if문 다 지나쳤다면 0 이라는 뜻
            # 방문 확인 후 큐에 해당 좌표 추가
            visited[dx][dy] = True
            queue.append((dx,dy))
    # return하지 못했다면 갈 수 없다는 것이므로 0 반환    
    return 0



for test_case in range(1,11):
    N = int(input())    # 입력

    grid = [list(input().strip()) for _ in range(100)]      #2차원 행렬
    visited = [[False for _ in range(100)] for _ in range(100)] # 방문 여부 확인용

    # 1은 벽, 0은 길, 2는 출발점, 3은 도착점
    pos = [(-1,0),(1,0),(0,1),(0,-1)]

    flag = 0        # 이중 for문 빠져나오기 위한 변수

    for i in range(0,100):
        for j in range(0,100):
            if grid[i][j] == '2':  # 시작지점이라면
                visited[i][j] = True    # 방문 표시
                print(f"#{test_case} {bfs(i,j)}")   # bfs 함수 진행
                flag = 1
                break
        if flag:
            break

    