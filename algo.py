T = int(input())


pos = [(-1,-1),(-1,1),(1,-1),(1,1)]

for test_case in range(1,T+1):
    n = int(input())

    dessert_list = [list(map(int,input().split())) for _ in range(n)]

    print(dessert_list[1][2])