# 클래스 정의
class Person: # 클래스
    blood_color = 'red'       # 속성(attribute)
    def __init__(self, name): # 메서드(함수)
        self.name = name
    def singing(self):
        return f'{self.name}가 노래합니다.'


# 인스턴스 생성
singer1 = Person('iu')
# 메서드 호출
print(singer1.singing())  
# 속성(변수) 접근
print(singer1.blood_color)