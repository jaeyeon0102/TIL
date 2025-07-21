# 모든 학생의 평균 점수를 계산하여 출력하시오.
# 80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
# 학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
# 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.

'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.

# 1번
students = {"Alice" : 85, "Bob": 78, "Charlie":92, "David":88, "Eve":95}
print("1. students type:" ,type(students))
print("학생들의 이름과 점수:",students)


avg = sum(students.values()) / len(students)

# 2번
print("2. 모든 학생의 평균 점수:",avg)


# 3번
std_avg = list(key for key ,val in students.items() if val>= 80)

print("3. 기준 점수(80)점 이상을 받은 학생 수:",std_avg)


# 4번
score = sorted(students.items(), key = lambda x : x[1], reverse=True)
print("4. 점수 순으로 정렬:")
for key, val in score:
   print(f"{key}: {val}")


# 5번
print("5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이:", score[0][1] - score[4][1])



# 6번
print("6. 각 학생의 점수가 평균보다 높은지 낮은지 판단:")
for key, val in students.items():
   if val < avg:
      print(f"{key} 학생의 점수({val})는 평균 이하입니다.")
   elif val >= avg:
      print(f"{key} 학생의 점수({val})는 평균 이상입니다.")