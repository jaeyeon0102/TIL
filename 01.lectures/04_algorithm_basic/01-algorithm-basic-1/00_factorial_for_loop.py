# 팩토리얼을 반복문으로 구현!
# 팩토리얼이 뭔가요? 3! -> 1*2*3


# 구하고자 하는 값 N
N = 5

# 최종 결과값
answer = 1
# 이제 1부터 N까지 answer에 곱해 나갈 수 있도록 순회

for num in range(1, N+1):
    answer *= num

print(answer)

#코드 실행은 ctrl + shift + f10