def merge_sort(arr):

    

    n = len(arr)

    if n <= 1:
        return arr
    
    mid = n//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # if left_half[-1] > right_half[-1]:
    #     cnt +=1

    return merge(left_half,right_half)

def merge(left, right):
    global cnt 
    if right[-1] < left[-1]:
        cnt += 1
    result = []
    i= 0
    j= 0
    while len(left) > i and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])

    return result


T = int(input())


for test_case in range(1,T+1):
    N = int(input())

    cnt = 0

    num_list = list(map(int,input().split()))

    result = merge_sort(num_list)

    print(f"#{test_case} {result[N//2]} {cnt}")