"""함수!!"""

'''일반적인 함수'''
# def add(a, b):
#     result = a + b
#     return result
# a = add(3, 4)
# print(a)

'''입력값이 없는 함수'''
# def say():
#     return 'Hi!'
# a = say()
# print(a)

'''결과값이 없는 함수'''
# def add(a, b):
#     print(f"{a}와(과) {b}의 합은 {a+b}입니다.")
# a = add(3, 4)  #오직 return을 통해서만 결과값을 돌려받을 수 있다. 따라서 변수에 add를 대입하면 NONE 출력
# print(a)     # NONE

'''매개변수를 지정하여 호출하기'''
# def add(a, b):
#     return a + b
# result = add(b=7, a=3) #매개변수를 지정하면 순서에 상과없이 사용가능
# print(result)

'''여러 개의 입력값을 받는 함수를 만들기'''
# def add_many(*args):  #매개변수 앞에 *를 붙이면 입력값을 전부 모아서 튜플로 만들어준다.
#     result = 0
#     for i in args:
#         result += i
#     return result

# result  = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(result)
'''응용!'''
# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# result = add_mul("add", 1, 2, 3, 4, 5)
# result2 = add_mul("mul", 1, 2, 3, 4, 5)
# print(result, result2)

'''키워드 피라미터'''
# def print_kwargs(**kwargs): #매개변수의 이름 앞에 **를 붙이면 매개변수는 딕셔너리가 되고 
#     print(kwargs)
# print_kwargs(a =1, name = "foo",age = 3) # 모든 key = value 형태의 결괏값이 딕셔너리에 저장

'''파이썬의 결괏값은 항상 하나이다.'''
# def add_and_mul(a, b):
#     return a+b, a*b   #결괏값이 a+b, a*b 두개처럼 보이지만 a+b, a*b를 합쳐 하나의 튜플로 리턴해준다.
# result = add_and_mul(3, 4)
# print(result)  #(7, 12) <-- 이 하나의 튜플 값을 두 개의 결과값처럼 받고 싶다면 아래와 같이 하면 된다.

# result1, result2 = add_and_mul(3, 4)
# print(result1, result2) # 결괏값 7과 12

#return문을 두번 쓰더라도 return을 만나면 함수를 빠져나가기 때문에 처음 만난 return 값 만이 함수의 결과값이 된다.

'''return문의 또다른 쓰임새'''
# def say_nick(nick):
#     if nick == "바보":
#         return
#     print(f"나의 별명은 {nick}입니다.")
# say_nick("바보")   # 즉 "바보"라는 값이 들어오면 return문을 통해 함수를 바로 빠져나가게 하는 것 while문의 break처럼 사용가능하다

'''매개변수의 초깃값 미리 설정하기'''

# def say_myself(name, old, man = True):  # man을 True로 지정해두면 자덩으로 설정됨! 매개변수 값이 항상 변하는 것이 아니라면 유용한 방법
#     print(f"나의 이름은 {name}입니다.")
#     print(f"저의 나이는 {old}살 입니다.")
#     if man: print("저는 남자입니다.")
#     else: print("저는 여자입니다.")

# say_myself("최지혁", 23) # = say_myself("최지혁", 23, True) 다음과 같은 결과를 도출한다.
# say_myself("최지순", 23, False) # False 를 넣어주면 당연히 반대가 출력된다.

'''초깃값을 설정할때 주의할 점!!'''
'''초깃값을 갖는 매개변수는 항상 뒤데두도록 하자'''
# 아래와 같은 형식은 오류가 발생함
#def say_myself(name, man = True, old): old와 man의 위치 변경은 불가능

'''함수에서 선언한 변수의 효력 범위'''
# a = 1
# def vartest(a): # 즉 함수안에서 사용된 변수는 함수 밖에는 어떠한 영향도 미치지 않는다. 
#     a += 1               # 하지만 다음 문단에서 보는 것처럼 함수 밖의 변수를 함수 안에서 사용할 수는 있다. 
#     return a
# df = vartest(a)
# print(a)
# print(df)

# a = 1
# def vartest():
#     global a  #이처럼 global 명령어를 사용하면 함수 밖의 변수를 함수 안으로 가져올 수는 있으나 사용 자제!!
#     a += 1                      # 함수는 독립적으로 존재하는게 좋음
# vartest()
# print(a)

""">>>>>>>>>>>>대망의 lambda(람다)함수!!!!!!!!!!!!!<<<<<<<<<<<<<"""
'''lambda 함수의 보다 자세한 내용은 개인공부 > lambda.py 파일을 참고 하도록 하자'''
# def를 사용할 정도로 복잡하지 않거나 사용할 수 없는 꽀예 쓰인다.
# 1회용 함수 혹은 예약어라고 함
'''람다의 기본 문법 --> lambda 매개변수1, ... ,매개변수n : 매개변수를 사용한 표현식'''
# add = lambda a, b:a+b
# result4 = add(3, 4)
# print(result4)

"""파일 읽고 쓰기!"""
'''파일 생성하기'''
# f = open("새 파일.txt", 'w') #여기서 'w'는 쓰기모드라는 의미! 'r'는 읽기모드 'a'추가모드 쓰기모드로 파일을 열면 해당 파일이 이미 존재할 경우 해당 파일 초기화
                             #쓰기모드로 파일을 열면 해당 파일이 이미 존재할 경우 해당 파일 초기화
# f.close() #close()는 생략해도 상관 없지만 닫아주는게 좋다 파일이 열려있는데 다시 사용하려 하면 오류 발생

'''파일을 쓰기모드로 열어 출력값 적기'''
# f = open("C:/Users/82103/OneDrive/바탕 화면/Pythonworkspace/새 파일.txt", 'w')
# for i in range(1, 11):
#     data = f"{i}번째 줄입니다.\n"
#     f.write(data) #<--- data를 파일 객체 f에 써라
# f.close()

"""프로그램의 외부에 저장된 파일을 읽는 여러가지 방법"""
'''readline 함수 사용하기''' '''가장 첫째줄을 출력'''
# f = open("C:/Users/82103/OneDrive/바탕 화면/Pythonworkspace/새 파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break # while함수를 활용해 파일 내의 모든 줄을 읽기
#     print(line)
# f.close()

'''readlines 함수 활용하기''' '''각 줄을 요소로 삼아 리스트 생성'''
# f = open("C:/Users/82103/OneDrive/바탕 화면/Pythonworkspace/새 파일.txt", 'r')
# lines = f.readlines() #readlines 함수는 파일 속 각각의 줄을 요소로 갖는 리스트로 돌려준다. 
# for line in lines:
#     print(line) #for문으로 리스트 요소를 하나씩 출력
# f.close()

'''read 함수 사용하기''' '''파일 전체 내용을 문자열로 돌려줌'''
# f = open("C:/Users/82103/OneDrive/바탕 화면/Pythonworkspace/새 파일.txt", 'r')
# data = f.read()
# print(data)
# f.close()

'''파일에 새로운 내용 추가하기'''
# f = open("C:/Users/82103/OneDrive/바탕 화면/Pythonworkspace/새 파일.txt", 'a')
# for i in range(11, 20):
#     data = f"{i}번째 줄입니다.\n"
#     f.write(data)  #<--- data를 파일 객체 f에 써라
# f.close()

'''with 문과 함께 사용하기''' '''with문을 사용하면 파일을 열고 닫는걸 자동으로 할 수 있다.'''
# with open("foo.txt", 'w') as f:
#     f.write("Life is too short, you need python")

'''sys 모듈로 매개변수 주기''' '<-- 좀 어려움'
import sys

args = sys.argv[1:]
for i in args:
    print(i)
