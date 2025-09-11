def get_minimum_coins_backtrack(coins, change):
    coins.sort(revese = True)
    min_coins = change

    result = {}


    def backtrack(remain , target, curr_comb, acc):
        '''

        '''
        if remain == 0:
            if acc < min_coins:
                min_coins = acc
    
    return result




# 사용 예시
coins = [1, 5, 10, 50, 100, 400, 500]  # 동전 종류
change = 882  # 잔돈

result = get_minimum_coins_backtrack(coins, change)
for coin, count in result.items():
    if count > 0:
        print(f"{coin}원: {count}개")
    