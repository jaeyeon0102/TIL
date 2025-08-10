def comb(arr, n):
    result = []  # 조합 결과를 담을 리스트

    # 종료 조건: n이 1이면 arr의 각 원소를 개별 리스트로 만들어 반환
    if n == 1:
        return [[i] for i in arr]

    # 재귀적으로 조합 생성
    for i in range(len(arr)):
        elem = arr[i]  # 현재 고를 원소 -> 하나 뽑고

        # arr[i+1:] → 현재 원소 이후의 원소들만 사용
        # n-1 → 하나를 골랐으니 남은 개수는 n-1
        for rest in comb(arr[i + 1:], n - 1):
            # 현재 원소(elem) + 나머지 조합(rest)을 합쳐서 결과에 추가
            result.append([elem] + rest) # -> 나머지 하나

    return result  # 최종 조합 리스트 반환



import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    matrix = [list(map(int, input().split(()))) for _ in range(N)]

    comb(matrix,N//2)