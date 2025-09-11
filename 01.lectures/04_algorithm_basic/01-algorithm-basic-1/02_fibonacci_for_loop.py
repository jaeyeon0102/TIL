def fibonacci_for_loop(n):
    # 기본 룰은 동일하게 적용해야 한다.
    # n이 0이면 0 반환
    # n이 1이면 1 반환
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #n이 2 이상인 경우
    else:
        # 내 이전의 두 항의 값이 무엇인지 알 수 있어야 함.
        # 이 else문에 올 수 있는 가장 적은 수 2를 기준으로 생각
        return fibonacci_for_loop(n-1) + fibonacci_for_loop(n-2)

# 사용 예시
print(fibonacci_for_loop(10)) # 55