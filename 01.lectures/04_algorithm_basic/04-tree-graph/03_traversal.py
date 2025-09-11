# 완전 이진 트리 기준 순회

# 전위 순회
def preorder_traversal(idx):
    #어디까지 순회해야 하나?
    # 순회 대상 범위를 벗어나지 않았다면
    if idx <= N:
        print(tree[idx], end=' ')
        # 이제 왼쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx*2)
        preorder_traversal(idx*2+1)

# 중위 순회
def inorder_traversal(idx):
    '''
        중위 순회란, 부모 노드 차례가 중간인 순회 방식
        즉, 왼쪽 서브 트리에 대한 처리가 우선 되어야 함
    '''
    if idx <= N:
        inorder_traversal(idx * 2)
        print(tree[idx], end=' ')
        inorder_traversal(idx * 2 + 1)

# 후위 순회
def postorder_traversal(idx):
    if idx <= N:
        postorder_traversal(idx * 2)
        postorder_traversal(idx * 2 + 1)
        print(tree[idx], end=' ')


N = 5
tree = [0, 'A', 'B', 'C', 'D', 'E']


'''
    트리 구조
        'A'
      /   \
   'B'    'C'
  /   \
'D'    'E'
'''

print('전위 순회')
preorder_traversal(1)  # 'A' 'B' 'D' 'E' 'C'
print()
print('중위 순회')
inorder_traversal(1)  # 'D' 'B' 'E' 'A' 'C'
print()
print('후위 순회')
postorder_traversal(1)  # 'D' 'E' 'B' 'C''A'