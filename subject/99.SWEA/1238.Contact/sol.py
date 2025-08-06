import sys

sys.stdin = open('input.txt')

from collections import deque

# param : 시작 노드 : 2
# return : result : 마지막 노드 리스트
def bfs(start_vertex, start_level):

    visited = set()             # 방문 여부

    queue = deque()             # 큐
    queue.append((start_vertex,0))  # 큐에 시작 노드 삽입
    visited.add(start_vertex)   # visited 시작노드 추가

    path[start_level].append(start_node)

    # 큐가 존재할 때
    while queue:
        node, level = queue.popleft()
        # node가 부모인 자식들을 neighbor에 넣어 순회
        for neighbor in adj_list.get(node, []):
            # 아직 방문하지 않은 노드라면
            if neighbor not in visited:
                path[level+1].append(neighbor)
                visited.add(neighbor)   # 방문 확인
                queue.append((neighbor,level+1))  # queue에 삽입



for test_case in range(1,11):
    # 데이터 길이, 시작 노드
    data_length, start_node = map(int, input().split())

    # 데이터
    data = list(map(int,input().split()))

    # 인접 리스트 생성
    adj_list = {data[node]: [] for node in range(0,len(data),2)}  
    
    # 데이터가 from, to , from , to 형식으로 되어있으므로 2칸씩 순회하며 저장
    for edge in range(0,len(data),2):
        u, v = data[edge], data[edge+1]
        adj_list[u].append(v)

    path = [[] for _ in range(101)]

    bfs(start_node, start_level=0)
    

    for level in reversed(range(len(path))):
        if path[level]:
            answer = max(path[level])
            break


    print(f"#{test_case} {answer}")