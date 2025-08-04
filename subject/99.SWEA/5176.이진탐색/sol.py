import sys

sys.stdin = open('input.txt')

T = int(input())

# 중위순회
def inorder(idx):
    if idx <= N:
        inorder(idx * 2)
        result.append(node[idx])
        inorder(idx * 2 + 1)



for test_case in range(1,T+1):
    N = int(input())

    node = list(range(N+1))
    result = []

    inorder(1)
    
    print(f"#{test_case} {result.index(1)+1} {result.index(N//2)+1}")