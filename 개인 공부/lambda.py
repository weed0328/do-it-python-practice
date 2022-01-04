# print((lambda x, y : x+y)(3, 4))

# add = lambda x, y : x+y
# print(add(3,4))

# lambdas = [lambda x:x+10, lambda x:x+100]
# print(lambdas[0](5))
# print(lambdas[1](4))

# def plus(a, b): print(a+b)
# plus(20, 50)
# t = plus
# t = (20, 50)

# fruit = {'apple':5, 'grape': 10, 'banana': 7, 'peach':3, 'melon':2}

# def f1(x):           # 이런 함수를 간단하게 람다로 지정이 가능하다.
#     return x[1]

# sorted1 = sorted(fruit.items(), key = f1)   #key다음에는 반드시 함수를 입력 받아야함 #따라서 17번 행 처럼 함수 식을 따로 만들어줘서 입력 가능
# print(sorted1)

# sorted1 = sorted(fruit.items(), key=lambda x:x[0])    #람다를 활용하면 함수를 따로 지정하지 않고 정렬가능하다.
# sorted2 = sorted(fruit.items(), key=lambda x:x[1])    #람다를 사용하면 코드가 간편해짐!

# print(sorted1)
# print(sorted2)

"""key가 없어도 람다 사용이 가능하다. 람다와 조건부 표현식 사용법"""
'''lambda 매개변수들(요소): 식1(최종적으로 하고자하는 식)(이러해라) if 조건식(이렇다면) else 식2, 리스트'''
# a = [i for i in range(1, 11)]
# list(map(lambda x: str(x) if x % 3 == 0 else x, a))

"""람다에서 조건부 사용시 주의할점!!"""
# 람다 표현식에서 if, else를 사용할 때는 :(콜론)을 붙이지 않음
# if, else와 분법이 다르므로 주의해야함
# 조건부 표현식은 식1 if 조건식 else 식2 형식으로 사용하며 식1은 조건식이 참일때 식2는 조건식이 거짓일때 시용할 식임
# 특히 람다 표현식에서는 if를 사용했다면 반드시 else를 사용해야함.
# if만 사용하면 SyntaxError: invaild syntax 애러 발생
# 람다 표현식에서는 elif 사용불가
# 조건이 많을 때는 if와 else를 번갈아가면서 써야함
# 식1 if 조건식1 else 식2 if 조건식2 else 식3 형식 밑이 예제 식

# a = [i for i in range(1, 11)]
# list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a ))
# print(a)

# 기본적으로 def 로표현되는 것들은 전부 lambda로 표현이 가능하나 너무 복잡하거나 복잡하지 않은데도 알아보기가 힘들다면 그냥 def 사용 권장
#밑에 식이 def 이용한 것
# a = [i for i in range(1, 11)]

# def f(x):
#     if x==1:
#         return str(x)
#     elif x==2:
#         return float(x)
#     else:
#         return x + 10

# print(list(map(f, a)))

"""map에 객체를 여러개 넣기"""
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8 ,10]
list(map(lambda x,y: x*y, a, b))
