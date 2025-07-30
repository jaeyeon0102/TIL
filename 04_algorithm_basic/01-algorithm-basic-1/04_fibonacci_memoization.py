def fibonacci_memoization(n):
    # n이 2 이상이고, memo[n]번쨰가 아직 계산되지 않았으면
        # 계산을 할 것이다

    if n>= 2 and memo[n] ==0:
        fibonacci_memoization(n-1) + fibonacci_memoization(n-2)



# 피보나치 수 10개 기록
n = 10
# 10개의 값을 기록? list
memo = [0] * (n+1)  # 0번 10까지 총 11개
memo[0],memo[1] = 0,1

