# import sys

# sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    V, E, node1, node2 = map(int,input().split())
    graph = {}

    edge = list(map(int,input().split()))
    
    
    children = {}
    parent = {}

    for i in range(0, len(edge), 2):
        p,c = edge[i] , edge[i+1]

        children.setdefault(p, []).append(c)
        parent[c] = p
    
    # print(parent)

    result1 = []

    idx = node1
    while (idx != None):
        if parent[idx]:
            result1.append(parent[idx]) 
            idx = parent[idx]
        else:
            idx = None

