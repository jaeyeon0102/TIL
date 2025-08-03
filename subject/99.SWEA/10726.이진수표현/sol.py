# import sys

# sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N,M = map(int, input().split())
    bin_num = 1 << N
    
    if (M % bin_num) == (bin_num - 1):
        print(f"#{test_case} ON")
    else:
        print(f"#{test_case} OFF")