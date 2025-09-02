# import sys

# sys.stdin = open('input.txt')

from collections import deque

def magnetic(mag_list, case):
    cnt = 0
    for col in range(case):
        queue = deque()
        for row in range(case):
            # print(mag_list[row][col])
            if (mag_list[row][col] == 1) and (not queue):
                queue.append(mag_list[row][col])
            elif (mag_list[row][col] == 2) and (queue):
                queue.pop()
                cnt += 1
    return cnt


for test_case in range(1,11):

    case = int(input())

    mag_list = [list(map(int,input().split())) for _ in range(case)]

    result = magnetic(mag_list, case)
    print(f"#{test_case} {result}")