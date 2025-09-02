T = int(input())


for test_case in range(1,T+1):
    N = int(input())

    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 6

    # i-1까지만 채워져 있을 때, i-2, i-3까지만 채워져있을 때 
    for i in range(4, N+1):
        dp[i] = dp[i-1] + 2*dp[i-2] + dp[i-3]

    print(f"#{test_case} {dp[N]}")