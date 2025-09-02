import sys

sys.stdin = open('input.txt')
# 0111011 0110001 011101101100010110001000110100100110111011
T = int(input())  # 테스트 케이스 개수 입력

# 7bit 암호화 숫자 딕셔너리 저장
pwd_dict = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001':5, '0101111': 6, '0111011':7, '0110111': 8, '0001011':9
}

# 출력을 위해 테스트 케이스는 1부터 시작
for test_case in range(1,T+1):
    # 배열 세로, 가로 입력
    height, width = map(int, input().split())
    # 2차원 배열로 값 입력 및 저장
    pass_scan = [(list(map(int,input()))) for _ in range(height)]

    # 첫 번쨰 열부터 순차적으로 1이 존재하는 열 찾기
    # 찾으면 password 변수에 해당 열의 모든 값을 join으로 합쳐서 문자열 저장 후 break 
    for i in range(height):
        if 1 in pass_scan[i]:
            password = ''.join(map(str,pass_scan[i]))
            break
    
    # 암호화 숫자들의 경우 마지막 값이 모두 1로 끝남
    # 이를 활용하여 password의 뒷쪽부터 값을 확인하여 처음으로 1이 나온 곳부터 앞의 56번째까지를 
    # pwd_code에 저장
    for i in range(len(password)-1,0,-1):
        if password[i] =='1':
            pwd_code = password[i-55:i+1]
            break
    
    # 7개씩 나눠서 순회하여 암호화 딕셔너리를 활용하여 실제 값 저장
    # [0, 7, 5, 7, 5, 5, 0, 2, 7]
    # 추후 암호 해독에 사용되는 홀수, 짝수 번째 계산과정의 편리함을 위해 pwd_num[0] = 0 삽입
    pwd_num =[0]
    for i in range(0,56,7):
        num = pwd_code[i:i+7]
        pwd_num.append(pwd_dict[num])
        
    # 암호 해독
    # 홀수 번째인 경우 해당 값에 3을 곱하여 cnt에 더함
    # 짝수 번째인 경우 해당 값을 cnt에 더함
    cnt = 0
    result = 0
    for i in range(1,len(pwd_num)):
        if (i % 2 == 1):
            cnt += pwd_num[i] *3
        elif (i %2 == 0):
            cnt += pwd_num[i]

    # 올바른 암호코드 확인
    # 10으로 나눴을 때 나머지가 존재하는지 확인
    # 존재하지 않으면 올바른 암호코드 이므로 result에 pwd_num의 모든 값을 합한 값 저장
    # 존재하면 잘못된 암호코드 이므로 result에 0 저장
    if cnt % 10 == 0:
        result = sum(pwd_num)

    else:
        result = 0

    # ouput
    print(f"#{test_case} {result}")
