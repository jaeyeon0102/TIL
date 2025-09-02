import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N,M = map(int, input().split())
    cheese = list(map(int,input().split()))
    pizza_wait_idx = 0
    queue = deque()

    for i in range(N):
        queue.append([i+1,cheese[i]])
        pizza_wait_idx += 1

    while (len(queue)>1):
        pizza = queue.popleft()
        pizza[1] = pizza[1] //2
        if pizza[1] == 0:
            if pizza_wait_idx < M:
                queue.append([pizza_wait_idx + 1,cheese[pizza_wait_idx]])
                pizza_wait_idx += 1
        else:
            queue.append(pizza)
             
    print(f"#{test_case} {queue[0][0]}")