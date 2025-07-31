for i in range(1, 4):  # i는 1에서 3까지의 값을 가지고, 첫 번째 자리의 숫자를 의미
    for j in range(1, 4):  # j는 1에서 3까지의 값을 가지고, 두 번째 자리의 숫자를 의미
        if j != i:  # j가 i와 같지 않은 경우에만 다음 블록을 실행
            for k in range(1, 4):  # k는 1에서 3까지의 값을 가지고, 세 번째 자리의 숫자를 의미
                if k != i and k != j:  # k가 i와 j와 같지 않은 경우에만 다음 블록을 실행
                    print(i, j, k)  # 서로 다른 세 숫자의 순열을 의미


def perm(selected, remain):
    '''
        selected : 선택된 값 목록
        remain : 선택되지 않고 남은 값 목록
    '''
    
    # 모든 요소를 선택할 것이니,,, 나머지가 없을 때까지
    if not remain: 
        print(*selected)
    else:
        for idx in range(len(remain)):
            # idx 번째의 요소를 선택
            select_item = remain[idx]

            remain_list = remain[:idx] + remain[idx+1:]
            perm(selected + [select_item],remain_list)

    
#초기 호출로 빈 리스트와 [1,2,3] 리스트 사용
perm([],[1,2,3])

