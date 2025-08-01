# import sys

# sys.stdin = open('input.txt')

T = int(input())

def cut_stick(stick):
    queue = []
    cnt = 0

    for char in stick:
        if char =='(':
            queue.append(char)
        elif char== ')':
            if check ==')':
                cnt += 1
                queue.pop()
            else:
                queue.pop()
                cnt += len(queue)
        check = char
    return cnt


for test_case in range(1,T+1):
    stick = str(input())
    
    result = cut_stick(stick)

    print(f"#{test_case} {result}")