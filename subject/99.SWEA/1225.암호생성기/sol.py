# import sys

# sys.stdin = open('input.txt')


def code_generation(queue):
    # 0이 나올 때까지
    while True:
        # 사이클 수에 맞게 순회
        for i in range(1,6):
            # q에 queue의 맨 앞 숫자 빼서 넣기
            q = queue.pop(0)
            # 만약 감소했을 때 0보다 작거나 같다면
            if q - i <= 0:
                # queue에 0을 뒷쪽에 넣고 종료
                q = 0
                queue.append(q)
                return queue
            # 아니라면 q-i 를 뒷쪽에 삽입
            else:
                q = q-i
                queue.append(q)
            

for test_case in range(1,11):
    # 입력 
    case_input = int(input())

    queue = list(map(int, input().split()))

    # 암호 함수 실행
    code = code_generation(queue)

    # 출력 형식 맞추기
    result = ' '.join(map(str,code))
    print(f"#{test_case} {result}") 