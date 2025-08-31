import sys
import heapq

sys.stdin = open('input.txt')

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
        if len(visited) == V + 1:
            break
            
        for next_node, next_weight in adj_list[end]:
            if next_node not in visited:
                heapq.heappush(min_heap, (next_weight, end, next_node))
    
    return mst_cost

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    adj_list = {i: [] for i in range(V + 1)}
    
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_list[n1].append((n2, w))
        adj_list[n2].append((n1, w))
    # print(adj_list)

    print(f"#{test_case} {prim(1, V, adj_list)}")