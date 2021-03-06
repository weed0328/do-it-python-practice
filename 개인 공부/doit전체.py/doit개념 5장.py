"""파이썬에 날개달기 클래스"""
'''기본적인 덧셈 계산기 함수'''
# result = 0
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
# class Calculator:
#     def __init__(self):             #과자 틀 --> 클래스
#         self.result = 0             #과자 틀로 만든 과자 --> 객체
    
#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator()  #<-- 객체1
# cal2 = Calculator()  #<-- 객체2
#                             # 이렇듯 클래스는 계산기가 여러대 필요하더라도 객체만 생성하면 되기 때문에 편함
# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

"백견이 불여일타 사칙연산 클래스 만들기"
'''클래스 구조 만들기'''
# class FourCal:
#     def setdata(self, first, second): #메서드(Method): 클래스 안에 구현된 함수를 메서드라고 한다.
#         self.first = first
#         self.second = second

# a = FourCal()    # <-- a 객체
# a.setdata(4, 2)
# print(a.first)

# b = FourCal()            # <-- b 객체      #이렇게 객체를 다르게 지정해주면 first 값에는 영향이 안감 
# b.setdata(5, 6)       # 하나의 class로 여러 장소에 사용가능
# print(b.first)

'''위에 있는 Fourclass class에 사칙연산 메서드 추가하기'''
# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
    
#     def add(self):
#         result = self.first + self.second
#         return result
    
#     def mul(self):
#         result = self.first * self.second
#         return result
    
#     def sub(self):
#         result = self.first - self.second
#         return result
    
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# b = FourCal()

# a.setdata(4, 2) <<-- 밑의 __init__을 사용하면 이 과정이 생략된다.
# b.setdata(3, 8)

# print(a.div())
# print(b.sub())

"""생성자 (Constructor)"""
'''만약 아래와 같이 setdata메서드를 수행하지 않으면 add메서드예써 오류 발생 '''
# a = FourCal()
# a.add()

'''때문에 객체의 초깃값을 설정해야하는 경우에는 생성자를 구현!!(보다 안전)'''
# class FourCal:
#     def __init__(self, first, second): # __init__ 생성자 메서드를 의미
#         self.first = first             # __init__ 메서드는 setdata와 이름만 다르고 전부 동일 다만 생성자로 인식되어
#         self.second = second           # 객체가 생성되는 시점에 자동으로 호출
    
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
    
#     def add(self):
#         result = self.first + self.second
#         return result
    
#     def mul(self):
#         result = self.first * self.second
#         return result
    
#     def sub(self):
#         result = self.first - self.second
#         return result
    
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal(4, 2)  # self = 생성되는 객체 a / first = 4 / second = 2
# print(a.mul())     # <= 제대로 작동하는 것을 볼 수 있음

"""클래스의 상속"""   '''상속이란 말 그대로 물려받는 것 클래스의 기능을 그대로 가져온다 생각'''
# class MoreFourCal(FourCal): # 이제  MoreFourCal 클래스는 FourCal의 모든 기능을 사용할 수 있다.
#     pass                    # 상속은 기존 클래스가 라이브러리로 제공되거나 수정이 허용되지 않는 상황에서 기존 클래스를 확장하고 싶을때 사용된다.
# b = MoreFourCal(4, 2)
# print(b.sub()) # 2 출력

# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result

# a = MoreFourCal(4, 2)
# print(a.pow())

'''메서드 오버라이딩(덮어쓰기)''' '''기존 클래스를 수정할때 사용'''
# class SafeFoulCal(FourCal):                   # 메소드 상속을 받은 후
#     def div(self):                            # 기존의 나눗셈 메서드를 입력
#         if self.second == 0: return 0         # 원하는 방향으로 수정
#         else: return self.first / self.second

# a = SafeFoulCal(4, 0)
# print(a.div())  #출력 0

"""클래스 변수""" '''클래스 변수는 객체 변수와 달리 클래스로 만든 모든 객체에 적용된다. a, b로 나눈다고 독립 X'''
# class Family:  
#     lastname = "김"  #클래스 변수

# print(Family.lastname)

# a = Family()
# b = Family()
# print(a.lastname) # "김"출력
# print(b.lastname) # "김"출력

# Family.lastname = "박"    # <-- 클래스 변수를 바꿨더니, a와 b가 둘 다 바뀜
# print(a.lastname) # "박" 출력
# print(b.lastname) # "박" 출력

""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>5-2 모듈<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
'''모듈이란? 함수나 변수 또는 클래스를 모아놓은 파일 즉, 파이썬 파일'''   # 확장자 '.py' 붙은 파일은 전부 모듈이라 보면 된다. 

'''모듈 불러오기''' '''모듈을 불러올떄는 같은 디렉토리 안에 있는걸 불러올 수 있다.'''
# import mod1
# print(mod1.add(3, 4))

# from mod1 import add
# print(add(5, 6))

# from mod1 import*  #'''<-- *를 붙이면 mod1의 모든 함수를 사용하겠다는 의미'''
# print(add(5, 6))

'''if __name__ == "__main__":의 의미'''
'''__name__변수란?'''
'''파이썬이 내부적으로 사용하는 특수한 변수의 이름으로 직접 파일을 실했을때는 __name__ == "__main__"이 참이 되어 실행이 되지만
다른 셀이나 모듈에서 import할 경우에는 거짓이 되어 if 다음문장이 실행되지 않는다.'''
# import mod1

"""클래스나 변수등을 포함한 모듈"""
#mod2 <-- class를 포함한 모듈
# import mod2
# print(mod2.PI)

# a = mod2.Math()
# print(a.solv(2))

"""패키지"""
# from game.sound import*
# echo.echo_test()

"""5-4 예외처리""" #클래스 죽이고 싶다...ㅠ 
'''오류 예외 처리기법'''

'''try, exept문'''

# # try:
# #     4/0
# # except ZeroDivisionError as e: 
# #     print(e)

# try:
#     a = [1, 2]
#     print(a[3])
# except IndexError:
#     print("인덱싱할 수 없습니다.")

# try:
#     a = [1, 2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e: #<-- 이렇게 합칠 수 있음
#     print(e)

'''오류 회피하기'''
# try:
#     f = open("나없는 파일", 'r')
# except FileNotFoundError:
    # pass

'''오류 일부러 발생시키기'''
# class Bird:
#     def fly(self): 
#         raise NotImplementedError   #반드시 fly함수를 구현하겠다는 의지 구현 안하면 어림도 없지 바로 오류

# class Eagle(Bird): #<-- Bird 상속받음
#     pass           # 구현 안했음으로 오류

# eagle = Eagle()
# print(eagle.fly())

# class Bird:
#     def fly(self): 
#         raise NotImplementedError   #반드시 fly함수를 구현하겠다는 의지 구현 안하면 어림도 없지 바로 오류
'''위와 같이 raise함수를 이용하여 예외를 일부러 발생기킬 수 있다.'''
# class Eagle(Bird): #<-- Bird 상속받음
#     def fly(self):            # 구현함!
#         print("very fast")           

# eagle = Eagle()
# eagle.fly()

'''예외 만들기'''
# # class MyError(Exception):
#     pass

def say_nick(nick):
    if nick =='바보':
        raise MyError()     # 닉네임이 바보면 오류를 일으킬 것
    print(nick)

try:
    say_nick("천사")        
    say_nick("바보")
except:
    print("허용되지 않는 별명입니다.")  # 오류대신 당므과 같은 문장을 출력할 것

#다음과 같은 방법도 있다.

try:
    say_nick("천사")        
    say_nick("바보")
except MyError as e:         #이거 그대로 출력하면 오류난다 따라서 밑에있는 __str__메서드를 구현해야함
    print(e)

class MyError(Exception):
    def __str__(self):  #__str__메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메세지이다.
        return "허용되지 않는 별명입니다."

