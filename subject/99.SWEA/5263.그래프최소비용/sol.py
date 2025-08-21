import sys
sys.stdin = open('input.txt')

def floyd_warshall(graph):
    n = len(graph) 
    
    for k_node in range(n):
        for start in range(n): # 시작노드
            for end in range(n): # 도착노드
                if graph[start][end] > graph[start][k_node] + graph[k_node][end]:
                    graph[start][end] = graph[start][k_node] + graph[k_node][end]
    return graph

T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    adj_matrix = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i != j and adj_matrix[i][j] == 0:
                adj_matrix[i][j] = float('inf')
    # print(adj_matrix)

    result = floyd_warshall(adj_matrix)

    max_cost = 0
    for i in range(N):
        for j in range(N):
            if i != j and result[i][j] <float('inf'):
                max_cost = max(max_cost,result[i][j])
    print(f"#{test_case} {max_cost}")