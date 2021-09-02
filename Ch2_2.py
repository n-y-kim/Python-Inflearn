class Car():
    """
    Car class
    Author: n-y-kim@github
    Date: 2021.09.02
    설명: 자동차 클래스. 회사 이름과 디테일 설명 입력 받음
    init, str, repr... : 인스턴스 함수
    _company, _details: 인스턴스 변수
    """

    #클래스 변수: 모든 인스턴스가 공유한다.
    car_count = 0
    
    def __init__(self, company, details) -> None:
        self._company = company
        self._details = details
        self.car_count = 100
        Car.car_count += 1

    def __str__(self) -> str:
        return 'str: {} - {}'.format(self.company, self.details)

    def __repr__(self) -> str:
        return 'repr: {} - {}'.format(self.company, self.details)

    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))
        print()

    def __del__(self):
        print()
        print("delete method called")
        Car.car_count -= 1


#self의 의미: 각 고유 클래스를 기반으로 생성된 인스턴스 내부의 고유의 값을 저장하기 위해 만들어진 지시어, 예약어
car1 = Car('Ferrai', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW',         {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi',         {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

#ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print()

print(car1._company == car2._company) #값 비교
print(car1 is car2) #ID가 다름(ID 비교)
print()

#dir & __dict__
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.__dict__)
print(car2.__dict__)

#Doctring
print(Car.__doc__)
print()

car1.detail_info()
Car.detail_info(car2)
car2.detail_info()
car3.detail_info()
print()

print(car1.__class__, car2.__class__, car3.__class__)
print()
#Car라는 class의 ID가 출력되고 있음
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))
print()

#클래스 변수 공유 확인
print(car1.car_count)
print(car2.car_count)
print(car3.car_count)
print()

#접근
print(car1.car_count)
print(Car.car_count)#정석

del car2
#삭제 확인
print(Car.car_count)

#인스턴스 네임스페이스에 없으면 상위에서 검색
#즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 없으면 상위(클래스 변수, 부모 클래스 변수))