# Hello, World!
print('Hello, World!') 
# str
print(type('Hello, World!')) 


bugs = 'roaches'
counts = 13
area = 'living room'
# Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')


my_str = 'hello'
# 인덱싱
print(my_str[1]) # e
# 슬라이싱
print(my_str[2:4]) # ll  # 2부터 4 앞까지 슬라이싱
# negative indexing도 가능
print(my_str[-2:-4]) # 위와 동일
print(my_str[0:5:2]) # he  # 0부터 5 앞까지 2칸씩 건너뛰기    

# 길이
print(len(my_str)) # 5

# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'


# replace
# 바꿀 대상 글자를 새로운 글자로 바꿔서 변환
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text)  # Hello, Python!

# strip
# 공백이나 특정 문자를 제거
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)  # 'Hello, world!'


# split
# 공백이나 특정 문자를 기준으로 분리
text = 'Hello, world!'
words = text.split(',')
print(words)  # ['Hello', ' world!']

# join
words = ['Hello', 'world!']
text = '-'.join(words)
print(text)  # 'Hello-world!'
