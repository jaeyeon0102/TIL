# 음수의 나눗셈,,
# print((-3)/2)
# print(int((-3)/2))


def dfs(depth, current_result, add, sub, mul, div):
    global max_num
    global min_num

    if depth == N:
        max_num = max(max_num, current_result)
        min_num = min(min_num, current_result)
        return

    if add > 0:
        dfs(depth+1, current_result + num_list[depth], add-1,sub,mul,div)
    if sub > 0:
        dfs(depth+1, current_result - num_list[depth], add,sub-1,mul,div)
    if mul > 0:
        dfs(depth+1, current_result * num_list[depth], add,sub,mul-1,div)
    if div > 0:
        dfs(depth+1, int(current_result / num_list[depth]), add,sub,mul,div-1)

T = int(input())

for test_case in range(1,T+1):
    max_num = -100000001
    min_num = 100000001
    N = int(input())
    op_list = list(map(int,input().split()))

    num_list = list(map(int, input().split()))

    dfs(1,num_list[0], *op_list)

    print(f"#{test_case} {max_num - min_num}")