import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]  # 초기 리스트

# 리스트를 최소 힙으로 변환
heapq.heapify(numbers)
print(numbers)

# 최소힙에 맞게 push 
heapq.heappush(numbers, -1)
print(numbers)

# 가장 작은 값 출력
# 최소 힙에 맞게 또 변환됨
smallest = heapq.heappop(numbers)
print(smallest)
print(numbers)

# 단, 주의 사항
# 이렇게 heap으로 만든 numbers를 리스트처럼 그냥 append 곤란함
numbers.append(-1)
print(numbers)