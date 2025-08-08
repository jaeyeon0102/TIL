import sys

sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 개수 입력

# 특정 노드의 모든 조상(부모, 부모의 부모...)을 리스트로 반환
def get_ancestors(node):
    path = [node]  # 자기 자신 포함
    while node in parent:  # 부모 정보가 있으면 계속 위로 올라감
        node = parent[node]
        path.append(node)
    return path

# 특정 노드를 루트로 하는 서브트리의 노드 개수 계산 (DFS 재귀)
def subtree(node):
    size = 1  # 자기 자신 포함
    for child in children.get(node, []):  # 자식 노드 목록 가져오기
        size += subtree(child)  # 각 자식의 서브트리 크기 더하기
    return size

for test_case in range(1, T+1):
    V, E, node1, node2 = map(int, input().split())
    # V: 정점 개수
    # E: 간선 개수
    # node1, node2: 공통 조상을 찾을 두 노드 번호

    edge = list(map(int, input().split()))  # 간선 정보 (부모, 자식) 순서로 입력됨

    children = {}  # 각 노드의 자식 리스트 저장
    parent = {}    # 각 노드의 부모 저장

    # 간선 정보로 children, parent 딕셔너리 구성
    for i in range(0, len(edge), 2):
        p, c = edge[i], edge[i+1]
        children.setdefault(p, []).append(c)  # 부모 p에 자식 c 추가
        parent[c] = p  # 자식 c의 부모는 p

    # 두 노드 각각의 조상 경로(자기 자신 포함) 구하기
    result1 = get_ancestors(node1)
    result2 = get_ancestors(node2)

    # 첫 번째 노드의 조상 중 두 번째 노드와 공통으로 갖는 첫 번째 조상 찾기
    for anc in result1:
        if anc in result2:
            common = anc  # 가장 가까운 공통 조상
            break

    # 공통 조상을 루트로 하는 서브트리 크기 구하기
    print(f"#{test_case} {common} {subtree(common)}")
