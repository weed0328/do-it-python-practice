"""내장함수"""
#abs 절댓값을 돌려준다.
from unittest import result


print(abs(-3.14))

#all
'''반복 가능한 자료형 함수를 받는다 모두 참이면 True 하나라도 거짓이면 False'''
print(all([1, 2, 3]))

#any all의 반대

#chr 아스키 코드

#dir 객체가 가지고 있는 변수나 함수를 보여줌
print(dir([1,2,3]))
print(dir({'1':'a'}))

#divmod(a, b) a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려준다.
print(divmod(7, 3))

#enumerate #순서가 있는 자료형(리튜문)을 입력받아 인덱스 값을 포함해서 객체로 돌려준다.
for i, name in enumerate(['동락', '지혁', '진구', '수민']):
    print(i, name)

#eval 실행 사능한 문자열을 입력받아 실행한 결괏값을 돌려준다.
print(eval('3 + 4'))
print(eval("'hi' + 'a'"))

#filter 함수 filter(함수이름, 반복가능한 자료형)
# def positive(l):
#     result = []
#     for i in l:
#         if i > 0: result.append(i)
    
#     return result

# print(positive([1, -3, 2, 0, -5, 6]))

'''위의 함수를 filter로 간단하게 만들 수 있음'''

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

'''바로 위의 함수를 lambda를 활용하면 더 쉽게 만들 수 있음'''

print(list(filter(lambda x:x > 0, [1, -3, 2, 0, -5, 6])))

# hex 정수값을 입력받아 16진수로 변환후 돌려준다.
print(hex(234))

#isinstance(object, class) 입력받은 인스턴스가 그 클래스의 인스턴스면 참 아니면 거짓을 구별해준다.
class Person: pass

a = Person()
b = 4
isinstance(a, Person)
isinstance(b, Person)

# map(f, iterable) 함수f와 반복가능한 자료형을 입력받고 자료형의 각 요소를 함수에적용시켜준다.

# def two_times(numberList):
#     result = []
#     for number in numberList: result.append(number*2)
#     return result

# result = two_times([1, 2, 3, 4])
# print(result)

'''위 함수를 map함수를 사용하여 간단하게 나타낼 수 있다.'''

def two_times(x): return x*2

print(list(map(two_times, [1, 2, 3, 4])))

'''lambda를 사용하면 더 간단해진다.'''
print(list(map(lambda x:x*2, [1, 2, 3, 4])))

#ord는 문자의 아스키 코드 값을 돌려줌

#pow(x, y) x의 y제곱한 결괏값을 돌려준다.
print(pow(2, 4))

#round 반올림 해주는 함수다.
round(4.6)
round(3.14568, 3) #소수점 3자리까지 반올림

#sorted 입력값을 정렬 후 리스트로 반환
sorted([3, 1, 2])
sorted(['b', 'c', 'a'])
sorted('zero')

#zip 함수 동일한 개수로 이루어진 자료형을 묶어주는 역할울 하는 함수이다.
list(zip([1, 2, 3], [4, 5, 6]))
list(zip('abc', 'def'))
