import sys

sys.stdin = open('input.txt')

T = int(input())

def get_ancestors(node):
    path = [node]
    while node in parent:
        node = parent[node]
        path.append(node)

    return path

def subtree(node):
    size = 1
    for child in children.get(node, []):
        size += subtree(child)
    return size


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
    
    result1 = get_ancestors(node1)
    result2 = get_ancestors(node2)

    for anc in result1:
        if anc in result2:
            common = anc
            break

    print(f"#{test_case} {common} {subtree(common)}")