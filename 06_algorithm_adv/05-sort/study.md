# 정렬

## 버블정렬

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
- 시간 복잡도 : O($n^2$)

### 정렬 과정

1. 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
2. 한 단계가  끝나면 가장 큰 원소가 마지막 자리로 정렬
3. 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품모양과 같다고 하여 버블 정렬이라고 함

### 코드

```python
def bubble_sort(arr):
    n = len(arr)  # 배열의 길이

    for i in range(n):
        for j in range(0, n - i - 1):  # 마지막 i개 요소는 이미 정렬되어 있으므로 비교에서 제외
            if arr[j] > arr[j + 1]:  # 현재 요소가 다음 요소보다 큰 경우
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 두 요소를 교환
```

## 삽입정렬

- 리스트를 정렬/미정렬로 나누고, ‘미정렬’ 부분의 원소를 ‘정렬된’ 부분의 올바른 위치에 삽입
- 시간 복잡도 : O($n^2$)

### 정렬 과정

1. 정렬할 자료를 두 개의 부분집합 S와 U로 가정
    1. 부분집합 S : 정렬된 앞부분의 언소들
    2. 부분집합 U : 아직 정렬되지 않은 나머지 원소들
2. 정렬되지 않은 부분집합 U의 원소를 하나씩 꺼내서 이미 정렬 되어있는 부분집합 S의 마지막 원소부터 비교하면서 위치를 찾아 삽입
3. 삽입 정렬을 반복하면서 부분집합 S의 원소는 하나씩 늘리고 부분집합 U의 원소는 하나씩 감소하게 됨
    1. 부분집합 U가 공집합이 되면 삽입정렬 완성 

### 코드

```python
def insertion_sort(arr):
    n = len(arr)  # 배열의 길이

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
```

## 카운팅정렬

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
- 제한사항
    - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
        - 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문
    - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 함
- 시간 복잡도 : O(n+k) : n은 리스트 길이, k는 정수의 최대값

### 코드

```python
def counting_sort(arr, max_value):
    n = len(arr)  # 배열의 길이
    count_arr = [0] * (max_value + 1)  # 최대값 + 1을 기준으로 임시 공간 할당
    result = [0] * n  # 정렬 결과를 저장할 변수

    # 각 요소의 빈도 계산
    for num in arr:
        count_arr[num] += 1

    # 각 숫자가 들어가야 할 인덱스를 저장하기 위해서, 누적합을 계산
    for i in range(1, max_value + 1):
        # dp와 같은 느낌으로
        # 이전까지 나온 수들의 합이 i가 놓을 수 있는 위치
        count_arr[i] += count_arr[i - 1]

    # 거꾸로 순회하면서, 현재 자신이 놓여야 하는 위치가 값을 놓고
    # 놓을 수 있는 위치를 -1 함
    for i in range(n - 1, -1, -1):
        val = arr[i]
        result[count_arr[val] - 1] = val
        count_arr[val] -= 1

    return result  # 정렬된 결과 반환
```

## 선택정렬

- 포켓볼 순서대로 정렬하기
    - 당구대 위에 있는 공 중 가장 작은 숫자의 공부터 골라서 차례대로 정리
- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치 교환하는 방식
- 시간 복잡도 : O($n^2$)

### 정렬 과정

- 주어진 리스트 중에서 최솟값 찾기
- 그 값을 리스트의 맨 앞에 위치한 값과 교환
- 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정 반복

### 코드

```python
def selection_sort(arr):
    n = len(arr)  # 배열의 길이

    # 맨 마지막 값은 굳이 비교할 필요가 없으므로, n-1까지만 순회
    for i in range(n - 1):
        min_idx = i  # 현재 위치를 최소값으로 가정

        # 이미 정렬된 원소 다음 위치부터 최소값 찾기
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:  # 현재 요소가 최소값보다 작은 경우, 최소값 인덱스 갱신
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 최소값과 현재 위치의 요소를 교환

```

## 병합정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
    - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
    - top-down 방식
- 시간 복잡도 O(nlogn)

### 코드

```python
def merge_sort(arr):
    n = len(arr)
    
    # 배열의 길이가 1 이하인 경우, 배열을 반환
    # 더 이상 나눌 수 없는 경우
    if n <= 1:
        return arr

    mid = n // 2  # 배열을 반으로 나눌 중간 인덱스를 구함
    left_half = arr[:mid]  # 왼쪽 절반 배열
    right_half = arr[mid:]  # 오른쪽 절반 배열

    # 왼쪽 절반과 오른쪽 절반을 재귀적으로 병합 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # 정렬된 두 절반을 병합
    # 더 이상 나눌 수 없는 부분까지 가면 아래 코드가 실행되고
    # 합쳐진 결과는 다시 15,16 라인에서 결과가 변수에 할당되면서
    # 재귀를 탈출하면서 결과를 구함
    return merge(left_half, right_half)

# 합치는 파트
def merge(left, right):
    result = []  # 병합된 결과를 저장할 리스트

    # 왼쪽 배열과 오른쪽 배열이 모두 비어있지 않은 동안 반복
    while left and right:
        # 왼쪽 배열의 첫 번째 요소가 오른쪽 배열의 첫 번째 요소보다 작은 경우
        if left[0] < right[0]:
            result.append(left.pop(0))  # 왼쪽 배열의 첫 번째 요소를 결과에 추가
        else:
            result.append(right.pop(0))  # 오른쪽 배열의 첫 번째 요소를 결과에 추가

    # 왼쪽 배열에 남은 요소들을 결과에 추가
    result.extend(left)
    # 오른쪽 배열에 남은 요소들을 결과에 추가
    result.extend(right)

    return result
```

## 퀵 정렬

- 주어진 배열을 두 개로 분할하고, 각각 정렬
- 퀵 정렬은 분할할 때, 기준 아이템(pivot item)을 중심으로, 이보다 작은 것은 왼편, 같거나 큰 것은 오른편에 위치
- 시간복잡도 O(nlogn)

### 코드

```python
# 분할하는 부분
def quick_sort(arr, start, end):
    # start >= end 라는 건 부분 배열의 길이가 0 or 1 이라는 소리이고
    # 그렇다는 건 퀵 정렬을 진행할 필요가 없다는 소리
    if start < end:
        # 피벗을 기준으로 리스트를 분할하고 피벗의 위치를 반환 
        p = partition(arr, start, end)
        
        # 피벗을 기준으로 분할된 두 부분을 재귀적으로 정렬
        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)

# 분할된 영역을 정렬하는 부분
def partition(arr, start, end):
    p = arr[start]  # 피벗을 리스트의 첫 번째 요소로 설정
    left = start + 1  # 왼쪽 포인터는 피벗 다음 요소부터 시작 
    right = end  # 오른쪽 포인터는 리스트의 끝에서 시작 

    while True:
        # 왼쪽에서 피벗보다 큰 값을 찾는다
        while left <= end and arr[left] < p:
            left += 1
        # 오른쪽에서 피벗보다 작은 값을 찾는다
        while right > start and arr[right] >= p:
            right -= 1
        # 두 인덱스가 교차하지 않으면 교환
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:  # 교차하면 중단하고, 아래 로직을 실행 (31 line)
            break
    
    # 피벗과 right 인덱스의 요소를 교환 
    arr[start], arr[right] = arr[right], arr[start]
    return right  # 피벗의 최종 위치 반환 
```