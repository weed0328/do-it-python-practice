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

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul("add", 1, 2, 3, 4, 5)
result2 = add_mul("mul", 1, 2, 3, 4, 5)
print(result, result2)