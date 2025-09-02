T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    num_list = list(map(int,input().split()))

    num_list.sort()

    print(f"#{test_case} {num_list[N//2]}")