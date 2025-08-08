# import sys

# sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N,M = map(int, input().split())
    # 왼쪽 시프트 : 2 ** N 과 동일
    # 오른쪽 시프트 :
    bin_num = 1 << N

    # bin_num -1 = 하위 N비트가 모두 1인 값
    # M % bin_num = M 을 2**N으로 나눈 나머지
    # 나머지 == 하위 N비트 값 -> 그게 전부 1인지 물어보는 것것
    if (M % bin_num) == (bin_num - 1):
        print(f"#{test_case} ON")
    else:
        print(f"#{test_case} OFF")