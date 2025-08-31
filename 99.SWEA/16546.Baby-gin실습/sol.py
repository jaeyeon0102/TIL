import sys

sys.stdin = open('input.txt')

def babygin(card_list, cnt):
    if cnt == 2:
        return True
    
    # triplet
    for i in range(10):
        if card_list[i]>=3:
            card_list[i] -= 3
            if babygin(card_list, cnt +1):
                return True
            else:
                card_list[i] += 3
    
    # run
    for i in range(8):
        if card_list[i] and (card_list[i] == card_list[i+1] == card_list[i+2]):
            card_list[i] -= 1
            card_list[i+1] -= 1
            card_list[i+2] -= 1
            if babygin(card_list, cnt +1):
                return True
            else:
                card_list[i] += 1
            card_list[i+1] += 1
            card_list[i+2] += 1
    return False



T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1,T+1):
    card_num = list(map(int,input().strip()))

    card_list = [0] *10

    for i in range(len(card_num)):
        card_list[card_num[i]] += 1

    if babygin(card_list, cnt =0):
        print(f"#{test_case} true")
    else:
        print(f"#{test_case} false")