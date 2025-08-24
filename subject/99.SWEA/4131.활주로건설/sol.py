import sys
sys.stdin = open('input.txt')

def check_road(arr, n, x):
    visited = [False]*n
    for i in range(n-1):
        if abs(arr[i] - arr[i+1]) >= 2:
            return False
        
        if arr[i] < arr[i+1]:
            for j in range(x):
                if i - j < 0 or arr[i-j] != arr[i] or visited[i-j]:
                    return False
                visited[i-j] = True
        elif arr[i] > arr[i+1]:
            for j in range(x):
                if i + 1 + j >= n or arr[i+1+j] != arr[i+1] or visited[i+1+j]:
                    return False
                visited[i+1+j] = True
    return True

T = int(input())

for test_case in range(1,T+1):
    n,x = map(int,input().split())

    land_list = [list(map(int,input().split())) for _ in range(n)]
    
    cnt = 0

    for i in range(n):
        if check_road(land_list[i],n,x):
            cnt += 1

    for j in range(n):
        col_list = [land_list[i][j] for i in range(n)]
        if check_road(col_list, n, x):
            cnt += 1            

                
    print(f"#{test_case} {cnt}")