'''
직원들의 키를 더해가며 합을 구하다가 
B보다 큰 탑이 발생하면 그 차를 구해서 제일 작은 차를 출력
dfs로 조합을 통해 합을 구하며 b와 크기 확인
min 값 출력하기
'''

def dfs(idx, top):
    global min_top
    if top >= B:
        min_top = min(min_top, top-B)
        return
    for i in range(idx,N+1):
        dfs(i+1,top + empl_list[i])   

    return 


T = int(input())

for test_case in range(1,T+1):
    N, B = map(int, input().split())
    min_top = 200000
    empl_list = [0]+list(map(int,input().split()))

    dfs(1, top = 0)

    print(f"#{test_case} {min_top}")