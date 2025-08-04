import sys

sys.stdin = open('input.txt')


 

T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1,T+1):
    N, M, L = map(int, input().split())
    leaf_node = [0] * (N+1)
    
    
    for _ in range(1,M+1):
        idx, value = map(int, input().split())

        leaf_node[idx] = value
    
    for i in range(N, 0, -1):
        left = i *2
        right = i * 2 +1

        if left <= N:
            leaf_node[i] += leaf_node[left]
        if right <= N:
            leaf_node[i] += leaf_node[right]

    print(f"#{test_case} {leaf_node[L]}")