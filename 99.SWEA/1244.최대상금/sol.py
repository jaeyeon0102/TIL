# import sys

# sys.stdin = open('input.txt')

def dfs(num,cnt):
    global max_num

    if cnt == change:
        max_num = max(int(num),max_num)
        return 
    if (num,cnt) not in visited:
        visited.add((num,cnt))
    
        num = list(num)
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                num[i], num[j] = num[j], num[i]
                # print(i)
                # print(num)
                dfs(''.join(num),cnt + 1)
                num[i], num[j] = num[j], num[i]


T = int(input())


for test_case in range(1,T+1):
    num, change = input().split()

    change = int(change)
    visited = set()
    max_num = 0
    
    dfs(num,0)
    
    
    print(f"#{test_case} {max_num}")