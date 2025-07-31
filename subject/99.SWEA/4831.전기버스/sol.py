import sys

sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 개수 입력

# 버스 충전 확인 함수
def bus_stop(K,N,m_list):
    result = 0 # 결과값
    bus = 0    # 버스 위치
    while True:  # 버스가 도착할 때까지 
        for i in range(bus + K,bus,-1):   # bus가 최대한으로 갈 수 있는 거리부터 -1씩 순회
            # 만약 버스 위치에 정류장이 있다면
            if i in m_list:
                # 버스는 해당 정류장 위치로 변경 및 움직인 횟수(결과값) +1
                bus = i
                result += 1
                break # 멈추고 다음으로
            # 만약 버스가 최종 목적지에 도착했다면
            elif i == N:
                # 버스를 최종 목적지로 변경 (이건 굳이 필요없었을지도)
                bus = i
                # result 반환
                return result
            # 버스가 최대한으로 이동 가능한 거리 내에 정류장이 없다면 갈 수 없음으로 판단
            elif i == bus+1:
                return 0
            
           
for test_case in range(1,T+1):        
    # result = 0
    K,N,M = map(int, input().split())

    m_list = list(map(int, input().split()))
    
    result = bus_stop(K,N,m_list)


    # ouput
    print(f"#{test_case} {result}")