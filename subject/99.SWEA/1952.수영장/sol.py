import sys

sys.stdin = open('input.txt')


T = int(input())

for test_case in range(1,T+1):
    day,month,third, year = map(int,input().split())

    plan = list(map(int,input().split()))

    money = [3001 for _ in range(12)]

    money[0] = min(month, day * plan[0])

    # 누적합
    for i in range(1,12):
        money[i] = money[i-1] + min(month, day * plan[i])

    money[2] = min(third, money[2])
    
    for i in range(3, 12):
        money[i] = min(money[i-1] + min(month, day*plan[i]), money[i-3] + third)

    result = money[-1]
    if result > year:
        result = year
    
    print(f"#{test_case} {result}")