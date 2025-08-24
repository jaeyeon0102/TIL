T = int(input())


for test_case in range(1,T+1):
    n, k = map(int,input().split())
    queue = list(input().strip())
    num_list = set()

    for i in range(n//4):
        for j in range(0,n,n//4):
            num = ''.join(queue[j:j+(n//4)])
            num_list.add(int(num,16))

        a = queue.pop(0)
        queue.append(a)
        
    num_list = sorted(num_list,reverse=True)
    print(f"#{test_case} {num_list[k-1]}")