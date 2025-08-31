# import sys

# sys.stdin = open('input.txt')

T = int(input())


# 잘린 막대기 개수 세기
def cut_stick(stick):
    # 스택 리스트 생성
    queue = []
    # 막대기 개수 세는 변수
    cnt = 0

    # 스틱 하나씩 순회
    for char in stick:
        # '('라면 추ㅏㄱ
        if char =='(':
            queue.append(char)
        # ')' 라면 이전 스틱이 ')' 인지 확인
        elif char== ')':
            # 이전 스틱도 ')'라면 하나의 막대기가 끝났다는 것
            if check ==')':
                # 개수 하나만 추가
                cnt += 1
                queue.pop()
            # 아니라면 레이저 발사함
            else:
                queue.pop()
                # 스택 길이만큼 추가
                cnt += len(queue)
        check = char
    return cnt


for test_case in range(1,T+1):
    # 스틱 입력 '()(((()())(())()))(())'
    stick = str(input())

    # 함수 결과 반환
    result = cut_stick(stick)

    print(f"#{test_case} {result}")