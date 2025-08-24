# import sys
# sys.stdin = open('input.txt')

def power_set(x,y,idx,acc,benefit):
    '''
    x,y : 현재 행,열 위치
    idx : 현재 선택할 대상 요소의 idx
    acc : 꿀통 개수 합
    benefit : 이익    
    '''

    global max_value
    if acc > C:
        return
    
    if idx == M:
        if max_value < benefit:
            max_value = benefit
        return

    now_benefit = data[x][y+idx]**2
    power_set(x,y,idx+1,acc+data[x][y+idx],benefit+now_benefit)
    power_set(x,y,idx+1,acc,benefit)


T = int(input())


for test_case in range(1,T+1):
    # 벌통 크기: N, 개수: M, 최대 양: C
    # 3 <= N <= 10, 1 <= M <= 5, N >= M, 10 <= C <= 30
    N, M, C = map(int, input().split())
    # 각 칸별 꿀의 양
    data = [list(map(int, input().split())) for _ in range(N)]

    # 최종 결괏값
    result = 0  


    for x in range(N):
        for y in range(N-M+1):
            max_value = 0
            power_set(x,y,0,0,0)
            A_max_value = max_value

            for k in range(x,N):
                for l in range(N-M+1):
                    if k == x and l < y+M: continue
                    max_value = 0
                    power_set(k,l,0,0,0)
                    B_max_value = max_value
                    result = max(A_max_value + B_max_value, result)

    print(f"#{test_case} {result}")