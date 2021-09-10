#Special Method(Magic Method)
#파이썬의 핵심(Data model) -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스
#클래스 안에 정의할 수 있는 특정한(Built in) 메소드

#기본형
print(int)
print(float)

#모든 속성 및 메소드 출력
#print(dir(int))
#print(dir(float))

n = 10

print(n+100)
print(n.__add__(100))
#print(n.__doc__)
print(n.__bool__(), bool(n))
print(n*100, n.__mul__(100))

print()
print()

#클래스 예제1
class Fruit: 
    def __init__(self, name, price) -> None:
        self._name = name
        self._price = price
    
    def __str__(self):
        return 'Fruit Class Info: {}, {}'.format(self._name, self._price)

    def __add__(self, x):
        return (self._price + x._price) * 0.8 #20퍼 할인한다고 했을때 더하기 결과값은

    def __sub__(self, x):
        return self._price - x._price

    #대소 비교
    def __le__(self, x):
        if self._price <= x._price:
            return True
        else: return False

    def __ge__(self, x):
        if self._price >= x._price:
            return True
        else: return False

#인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1 + s2)
#print(s1.__add__(s2))

print()
print(s1 - s2)

print()
print(s1 >= s2)
print(s1 <= s2)

print()
print(s1)