#Special Method(Magic Method)
#파이썬의 핵심(Data model) -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스
#클래스 안에 정의할 수 있는 특정한(Built in) 메소드

#클래스 예제2
#벡터(x,y)
#Max((5,10))=10

class Vector:
    #packing & unpacking?
    def __init__(self, *args) -> None:
        """
        Create a vector, example: v = Vector(5,10)
        """

        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self) -> str:
        '''Return the vector informations'''
        return 'Vector(%r, %r)' %(self._x, self._y)

    def __add__(self, other):
        '''Return added vector'''
        return Vector(self._x + other._x, self._y + other._y)        

    def __mul__(self, x):
        '''Return added vector'''
        return Vector(self._x * x, self._y * x)        
    
    def __bool__(self):
        return bool(max(self._x, self._y)) #0,0인지 확인하는 메소드

print(Vector.__init__.__doc__)

#Vector instance 생성
v1 = Vector(5,7)
v2 = Vector(23, 35)
v3 = Vector()

#매직메소드 출력
print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2), bool(v3))

if bool(v3):
    print('ok')
else:
    print('error')