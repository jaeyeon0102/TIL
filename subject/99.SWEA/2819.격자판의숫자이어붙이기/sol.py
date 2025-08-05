def dfs(x,y,check):
    # 문자열 길이가 7이면 result에 저장 및 반환
    if (len(check)) == 7:
        result.add(check)
        return 

    # 동서남북 사방 순회
    for i in range(4):
        # 각 x, y 값을 변경하여 이동
        dx, dy = x + pos[i][0] , y + pos[i][1]
        # 격자판을 넘어가지 않도록 
        if (0 <= dx < 4) and (0 <= dy < 4):
            dfs(dx,dy,check + grid_list[dx][dy])




T = int(input())

for test_case in range(1, T+1):
    grid_list = [list(map(str,input().split())) for _ in range(4)]

    # 동서남북 좌표 지정
    pos = [(-1,0),(1,0),(0,-1),(0,1)]

    # 중복제거되는 set 집합 사용
    result = set()

    # 모든 격자 탐색
    for i in range(4):
        for j in range(4):
            dfs(i, j, grid_list[i][j])
            

    print(f"#{test_case} {len(result)}")