import sys

sys.stdin = open('input.txt')

def inorder(idx):
    if idx <= N:
        inorder(idx * 2)
        print(tree[idx], end='')
        inorder(idx * 2 + 1)



for test_case in range(1,11):
    N = int(input())

    tree = [0] * (N+1)
    
    for _ in range(N):
        value = list(map(str,input().split()))
        tree[int(value[0])] = value[1]

    print(f"#{test_case}",end=' ')
    inorder(1)
    print()