import sys

sys.stdin = open('input.txt')


T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1,T+1):
    card_num = list(map(str, input()))

    card_list = [0 for _ in range(10)]

    for i in range(len(card_num)):
        card_list[int(card_num[i])] += 1

    print(card_list)