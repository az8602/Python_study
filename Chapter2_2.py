# Chapter02-02

class Car():
    """
    Car class
    Author : Lee
    Date : 2022.07.15
    사용법 : ~~
    """

    # 클래스 변수
    # --> 스코프 개념 찾고 정리하기
    # 모든 인스턴스가 공유한다
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        # 존재 시 self의 car_count를 먼저 출력함(car1.car_count)
        # self.car_count = 10
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # representation
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

# Self의 의미 == 인스턴스(instance)
car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

# 다르다
print(car1._company == car2._company)
print(car1 is car2)

# dir 과 __dict__의 차이

# dir : 해당 인스턴스가 가지고 있는 모든 매직메서드를 리스트형태로 보여준다
# 값을 보여주지 않고, 상위로부터 상속받는 모든 것도 보여줌
print(dir(car1))
print(dir(car2))


print()
print()

# __dict__ : 내 네임스페이스만 보고 싶다, 내용도 보여줌, 딕셔너리 형태
print(car1.__dict__)
print(car2.__dict__)

# Docstring
# 위에서 쓴 """내용이 나온다
print(Car.__doc__)
print()

# 실행
car1.detail_info() # 이 때 id는 id(car1)과 동일
car2.detail_info()

# 비교
# Class의 id값을 본것이기 때문에 동일하다
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))

# 에러
# detail_info()는 self가 필요하다고 합니다
# 클래스.함수(인스턴스)로는 가능합니
car1.detail_info() # Self가 자ㄴ동으로
Car.detail_info() # 작동 안됨(에러)
Car.detail_info(car1)

# 공유하기
print(car1.car_count)
print(car1.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

# 삭제 확인
del car2
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스 변수))
