import sys

sys.stdin = open('input.txt')


def find_set_pc(x):
    """경로 압축이 적용된 find_set"""
    
    if x == parent[x]:
        return parent[x]
    
    parent[x] = find_set_pc(parent[x])
    return parent[x]

def union(x, y):
    """두 집합을 합치기"""
    root_x = find_set_pc(x)
    root_y = find_set_pc(y)
    # print(root_x,root_y)
    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())

for test_case in range(1,T+1):
    n, m = map(int,input().split())
    m_list = list(map(int,input().split()))

    parent = [i for i in range(n+1)]
    
    

    for i in range(0,len(m_list),2):
        union(m_list[i],m_list[i+1])

    cnt = 0
    for i in range(1,n+1):
        if find_set_pc(i) == i:
            cnt += 1

    print(f"#{test_case} {cnt}")