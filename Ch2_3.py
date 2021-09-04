class Car():
    """
    Car class
    Author: n-y-kim@github
    Date: 2021.09.04
    설명: 자동차 클래스. 회사 이름과 디테일 설명 입력 받음
    init, str, repr... : 인스턴스 함수
    _company, _details: 인스턴스 변수

    Description: Class, Static, Instance Method
    """

    #클래스 변수: 모든 인스턴스가 공유한다.
    price_per_raise = 1.0
    
    def __init__(self, company, details) -> None:
        self._company = company
        self._details = details

    def __str__(self) -> str:
        return 'str: {} - {}'.format(self.company, self.details)

    def __repr__(self) -> str:
        return 'repr: {} - {}'.format(self.company, self.details)

    #Instance Method
    #self: 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))
        print()

    #Instance Method
    def get_price(self):
        return 'Before Car Price -> company: {}, price: {}'.format(self._company, self._details.get('price'))

    def get_price_cal(self):
        return 'After Car Price -> company: {}, price: {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    #Class Method
    @classmethod
    def raise_price(cls, per):
        #cls = Car
        if per <= 1: 
            print("Please Enter 1 or More")
            return
        cls.price_per_raise = per
        print('Succeed! Price Increased')
    
    #Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This car is {}'.format(inst._company)
        else: return 'Sorry. This car is not BMW'
    




#self의 의미: 각 고유 클래스를 기반으로 생성된 인스턴스 내부의 고유의 값을 저장하기 위해 만들어진 지시어, 예약어
car1 = Car('Ferrai', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW',         {'color' : 'Black', 'horsepower': 270, 'price': 5000})

#전체정보
car1.detail_info()
car2.detail_info()

#가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())
print()

#가격정보(인상 후)
#Car.price_per_raise = 1.4 #직접 접근해서 수정하는 것은 좋은 방법이 아님! 객체 특유의

print(car1.get_price_cal())
print(car2.get_price_cal())
print()

#Class Method사용
Car.raise_price(1.5)
print(car1.get_price_cal())
print(car2.get_price_cal())
print()

#Static Method사용
#인스턴스 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
#클래스로 호출
print(Car.is_bmw(car1)) #유연함. 이것도 가능
