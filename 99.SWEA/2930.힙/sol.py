import sys

sys.stdin = open('input.txt')

import heapq

T = int(input())


for test_case in range(1,T +1):
    op_num = int(input())
    max_heap = []
    result = []

    for op in range(op_num):
        num = list(map(int, input().split()))
        if num[0] == 1:
            heapq.heappush(max_heap, -num[1])

        elif num[0] == 2:
            if max_heap:
                result.append(-heapq.heappop(max_heap))
            else:
                result.append(-1)

    print(f"#{test_case}",end=' ')
    print(*result)