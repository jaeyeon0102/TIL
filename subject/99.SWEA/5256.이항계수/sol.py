T = int(input())

for test_case in range(1,T+1):
    n,a,b = map(int,input().split())
    result = 1
    # print(result)
    for i in range(1,a+1):
        result += result * (n-i)
        # print(i,result)
    for i in range(a,1,-1):
        # print(i)
        result //= i

    # print(result)
    print(f"#{test_case} {result}")