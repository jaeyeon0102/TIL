import sys

sys.stdin = open('input.txt')


T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1,T+1):
    card_num = list(map(int, input().split()))
    