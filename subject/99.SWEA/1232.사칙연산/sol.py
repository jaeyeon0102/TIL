import sys

sys.stdin = open('input.txt')

def postorder(idx):
    # 숫자면 그냥 반환
    if isinstance(tree[idx],int):
        return tree[idx]

    # 연산자, 왼쪽, 오른쪽 자식
    oper, left ,right = tree[idx]
    left_value = postorder(left)
    right_value = postorder(right)

    # oper에 따라 값 리턴
    if oper == '+':
        return left_value  + right_value
    if oper == '-':
        return left_value  - right_value
    if oper == '*':
        return left_value  * right_value
    if oper == '/':
        return left_value  // right_value


for test_case in range(1,11):
    N = int(input())

    # 노드 수 + 1만큼 None 넣어두기 (1부터 시작할 예정)
    tree = [None] * (N+1)
    
    # 1부터 N까지 순회
    for _ in range(1,N+1):
        # [노드번호, 값, 왼쪽 자식, 오른쪽 자식]
        line = input().split()
        idx = int(line[0])

        # 만약 line이 총 4개 들어왔다면 연산자 노드이므로 
        if len(line) == 4:
            tree[idx] = (line[1], int(line[2]), int(line[3]))
        # 아니면 그저 숫자
        else:
            tree[idx] = int(line[1])
    
    result = postorder(1)

    print(f"#{test_case} {result}")