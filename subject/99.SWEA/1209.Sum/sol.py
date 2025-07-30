import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = input()
    # 100 x 100을 2차원 리스트로 받아야 함
    # 즉, 한 번 입력받은 한 줄에 100개의 숫자가 공백을 기준으로 문자열로 오게 됨

    data = [] #2차원 배열을 만들기 위한 리스트
        # 각 공백 기준으로 쪼개진 문자열을 정수로 바꾸기
    data = [list(map(int, input().split())) for _ in range(100)]
    print(data)