"""파이썬에 날개달기 클래스"""
'''기본적인 덧셈 계산기 함수'''

result = 0
# def add(num):
#     global result  #global로 밖의 result를 가져와 result값을 계속 갱신한다.
#     result += num
#     return result

# print(add(3))
# print(add(4))

'''만약 두개의 계산기가 필요하다면?'''
# result1 = 0
# result2 = 0

# def add1(num):                 #함수를 두개 지정해주면 되지만 코드가 길어지고 귀찮음
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))

'''class를 사용하여 두개의 계산기 간단하게 표현하기'''
class Calculator:
    def __init__(self):             #과자 틀 --> 클래스
        self.result = 0             #과자 틀로 만든 과자 --> 객체
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()  #<-- 객체1
cal2 = Calculator()  #<-- 객체2
                            # 이렇듯 클래스는 계산기가 여러대 필요하더라도 객체만 생성하면 되기 때문에 편함
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

"백견이 불여일타 사칙연산 클래스 만들기"
'''클래스 구조 만들기'''
class FourCal:
    def setdata(self, first, second): #메서드(Method): 클래스 안에 구현된 함수를 메서드라고 한다.
        self.first = first
        self.second = second
a = FourCal()
a.setdata(4, 2)
print(a.first)

b = FourCal()
b.setdata(5, 6)
print(b.first)