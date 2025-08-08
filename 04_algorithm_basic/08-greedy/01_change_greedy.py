coins = [1, 5, 10, 50, 100, 500]  # 동전 종류
change = 882  # 잔돈


'''
    거스름돈 문제 그리디로 해결
    가장 큰 거스름돈을 먼저 거슬러주고, 
    남은 금액을 다음 단위로 해결
'''

def get_minimum_coins(coins, change):
    result = {}

    # 가장 큰 coins에서 빼나갈 것이다 -> 오름차순
    coins.sort(reverse=True)

    # 코인 종류별로 change에서 제거
    for coin in coins:
        count = 0
        while change >= coin:
            change -= coin
            count += 1
            result[coin] = count

    return result 


# 아래의 경우라면 어떨까?
coins = [1, 5, 10, 50, 100, 400, 500]  # 동전 종류
change = 882  # 잔돈

result = get_minimum_coins(coins, change)
for coin, count in result.items():
    print(f"{coin}원: {count}개")
