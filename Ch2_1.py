#Chapter 02 - 01
#객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지,
#                        유지보수, 대형 프로젝트
#규모가 큰 프로젝트(프로그램) -> 함수 중심일 때는 -> 데이터 방대 -> 복잡
# 클래스 중심일때는 -> 데이터 중심 -> 객체로 관리

#일반적인 코딩

car_company_1 = "Ferrari"
car_detail_1 = [ 
    {'color' : 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

car_company_2 = "BMW"
car_detail_1 = [ 
    {'color' : 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

car_company_2 = "Audi"
car_detail_1 = [ 
    {'color' : 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

#리스트 구조
#관리하기가 불편
#인덱스 접근 시 실수 가능성, 삭제 불편
car_cmpany_list = [ 'Ferrari', 'BMW', 'Audi' ]
car_detail_list = [
    {'color' : 'White', 'horsepower': 400, 'price': 8000},
    {'color' : 'Black', 'horsepower': 270, 'price': 5000},
    {'color' : 'Silver', 'horsepower': 300, 'price': 6000}
]

del car_cmpany_list[1]
del car_detail_list[1]

print(car_cmpany_list)
print(car_detail_list)

print()
print()

#딕셔너리 구조
#코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dics = [
    {'car_company': 'Ferrai', 'car_detail':
        {'color' : 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'BMW', 'car_detail':
        {'color' : 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail':
        {'color' : 'Silver', 'horsepower': 300, 'price': 6000}}
]

del car_dics[1]
print(car_dics)

print()
print()

#클래스 구조
#구조 설계 후 재사용성 증가, 코드 반복 최소
#메소드 활용
class Car():
    def __init__(self, company, details) -> None:
        self.company = company
        self.details = details

    def __str__(self) -> str:
        return 'str: {} - {}'.format(self.company, self.details)

    def __repr__(self) -> str:
        return 'repr: {} - {}'.format(self.company, self.details)


car1 = Car('Ferrai', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW',         {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi',         {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

print(car1)
print(car2)
print(car3)

print()

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print()

print(dir(car1))
print()
print()

car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)
print()
print()

for car in car_list:
    print(repr(car))