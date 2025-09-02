import sys

sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    # N: 노드 개수, M: 리프 노드 개수, L: 값을 출력할 노드 번호

    leaf_node = [0] * (N + 1)  # 1번 인덱스부터 사용, 노드 값 저장용 리스트

    # 리프 노드 값 입력
    for _ in range(1, M+1):
        idx, value = map(int, input().split())
        leaf_node[idx] = value  # 해당 노드 위치에 값 저장

    # 부모 노드 값 계산 (역순으로 올라가면서 계산)
    for i in range(N, 0, -1):
        left = i * 2       # 왼쪽 자식 인덱스
        right = i * 2 + 1  # 오른쪽 자식 인덱스

        # 왼쪽 자식이 존재하면 더하기
        if left <= N:
            leaf_node[i] += leaf_node[left]
        # 오른쪽 자식이 존재하면 더하기
        if right <= N:
            leaf_node[i] += leaf_node[right]

    # L번 노드의 값 출력
    print(f"#{test_case} {leaf_node[L]}")
