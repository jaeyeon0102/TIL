import sys
sys.stdin = open('input.txt')

import heapq

def prim(start_node, V, adj_list):
    # MST에 포함된 정점을 기록할 집합
    visited = {start_node}

    # (가중치, 시작 정점, 끝 정점) 형태로 저장할 최소 힙
    min_heap = [(w, start_node, e) for e, w in adj_list[start_node]]
    # 힙으로 변경
    heapq.heapify(min_heap)

    # 가중치 합
    mst_cost = 0

    while min_heap:
        weight, start, end = heapq.heappop(min_heap)

        if end in visited:
            continue

        visited.add(end)
        mst_cost += weight

        # MST에 모든 정점이 포함되면 종료
        if len(visited) == V:
            break
            
        for next_node, next_weight in adj_list[end]:
            if next_node not in visited:
                heapq.heappush(min_heap, (next_weight, end, next_node))
    
    return mst_cost

T = int(input())


for test_case in range(1,T+1):
    N = int(input())

    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    E = float(input())

    edges = []
    adj_list = {i: [] for i in range(N)}

    for i in range(N):
        for j in range(i+1,N):
            cost = E *((x_list[i]-x_list[j]) **2 +(y_list[i] - y_list[j]) **2)
            adj_list[i].append((j,cost))
            adj_list[j].append((i,cost))
        
    print(f"#{test_case} {round(prim(0,N,adj_list))}")