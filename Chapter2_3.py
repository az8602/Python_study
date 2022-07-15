# Chapter02-03

class Car():
    """
    Car class
    Author : Lee
    Date : 2022.07.15
    Description : Class, Static, Instance Method
    """
    # 클래스 변수
    # 모든 인스턴스가 공유한다
    price_per_raise = 1.2

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # representation
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    # cls를 받음(class state)
    @classmethod # 데코레이터
    def raise_price(cls, per):
        cls.price_per_raise
        if per <= 1:
            print("Please Enter 1 Or More")
            return
        cls.price_per_raise = per
        print("Succeed! price inceased.")

    # Static Method
    # 어떠한 특정 파라미터를 받지 않음(자유롭게)
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is {}'.format(inst._company)


# Self의 의미 == 인스턴스(instance)
car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})

# 전체정보 출력
car1.detail_info()
car2.detail_info()

# 가격정보 출력(직접 접근)
# 이런식으로는 접근하지 않음(큰 문제가 생길 수 있다)
print(car1._details.get('price'))
print(car2._details['price'])

# 가격정보 출력(Method)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(직접 접근)
# 클래스 변수도 직접 접근 하는 것이 좋지 않다
Car.price_per_raise = 1.4

# 가격 인상(Method)
Car.raise_price(1.6)

# 가격 인상 반영(Method)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 자동차 종류 확인(Static Method)
# 클래스로 호출할 수도 있다
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car1)) # 유연하다
print(Car.is_bmw(car2))