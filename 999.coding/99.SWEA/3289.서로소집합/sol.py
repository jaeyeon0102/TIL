import sys

sys.stdin = open('input.txt')



def find_set_pc(x):
    
    if parent[x] != x:
        parent[x] = find_set_pc(parent[x])
    return parent[x]

def union(x, y):
    rx,ry = find_set_pc(x),find_set_pc(y)
    
    if rx>ry:
        parent[rx] = ry
    elif rx < ry:
        parent[ry] = rx
        

T = int(input())


for test_case in range(1,T+1):
    n,m = map(int,input().split())

    parent = [i for i in range(n+1)]
    ans = ''
    for i in range(m):
        check, a, b = map(int,input().split())

        if check:
            if find_set_pc(a) == find_set_pc(b):
                ans += '1'
            else:
                ans += '0'
        else:
            union(a,b)

    print(f"#{test_case} {ans}")