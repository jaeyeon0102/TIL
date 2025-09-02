import sys
sys.stdin = open('input.txt')


def dfs(idx, total_size, total_price):
    global max_price

    if total_size > N:
        return

    if idx == M:
        max_price = max(max_price, total_price)
        return

    dfs(idx+1, total_size+box_list[idx][0], total_price+ box_list[idx][1])
    dfs(idx+1, total_size, total_price)

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int,input().split())

    box_list = []

    max_price = 0

    for i in range(M):
        size , price = map(int,input().split())

        box_list.append((size,price))

    dfs(0,0,0)
    
    print(f"#{test_case} {max_price}")