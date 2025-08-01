arr = [1,2,3]
n = len(arr)
subset = []
# 모든 경우의 수에 대해 조회
# for idx in range(2**n):
for idx in range(1<<n):
    print(idx)

