# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1.intersection(s2))
# print(s1|s2)
# print(s1.union(s2))
# print(s1-s2)
# print(s1.difference(s2))
# s1.add(7)
# print(s1)
# s1.update([8, 9, 10])
# print(s1)
# s1.remove(7)
# print(s1)

'''불자료형'''
# a = True
# b = False
# print(type(a))
# print(type(b))
# print(1==1)
# from copy import copy
# a = [1, 2, 3, 4]
# b = a[:]
# b = copy(a)


# [a, b] = ['python', 'life']
# (c, d) = 'iphone', '13pro'
# a, b = c, d

'''doit Q1'''
# dic = {'국어': 80, '영어':75, '수학':55} 
# a = dic['국어'] + dic['영어'] + dic['수학']
# ave = a
# print(ave)

# '''doit Q3'''
# pin = "000328-1068234"
# yyyymmdd = pin[:6]
# num = pin[7:]
# print(yyyymmdd)
# print(num)

# '''doit Q3'''
# a = "a:b:c:d"
# b = a.replace(":", "#")
# print(b)

# '''doit Q4'''
# a = [1, 3, 5, 4, 2]
# a.sort()
# a.reverse()
# print(a)

# '''doit Q5'''
# a = ['Life', 'is', 'too', 'short']
# result = " ".join(a)
# print(result)

# '''doit Q8'''
# a = 1, 2, 3
# a = a + (4,)
# print(a)

# '''doit Q9'''
# ''' 딕셔너리의 키값에는 변하는 값인 리스트를 집어넣을 수가 없다.'''

# '''doit Q10'''
# a = {'A':90, 'B':80, 'C':70}
# result = a.pop('B')
# print(a)
# print(result)

# '''doit Q11'''
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = set(a)
# b = list(aSet)
# print(b)

# '''doit Q12'''
# a = b = [1, 2, 3]
# a[1] = 4
# print(b)

'''>>>>>>>>>>>>>>>>>>연습문제 2장<<<<<<<<<<<<<<<<<<<<<'''
"Q2"
# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         result += i
#     i += 1
# print(result)

"Q3"
# i = 0
# while True:
#     i += 1
#     if i > 5:break
#     print(i*'*')

'Q4'
# for i in range(1, 101):
#     print(i)

'Q5'
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for score in A:
#     total += score
# ave = total / 10
# print(ave)

'Q6'
# numbers = [1, 2, 3, 4, 5]
# result = [n*2 for n in numbers if n % 2 == 1]
# print(result)

'''4장 연습문제'''
'Q1'
# from os import replace


# def is_odd(number):
#     if number % 2 == 1: return True
#     else: return False
# result = is_odd(3)
# print(result)

'Q1 lambda 함수 이용하기'
# lol = lambda x : True if x % 2 == 1 else False
# lol(6) 

'Q2'
# import sys
# def avg_numbers(*args):
#     result = 0 
#     for i in args:
#         result += i
#     return print(result / len(args))

# avg_numbers(1, 2, 3, 4, 5)

'Q3'
# input1 = int(input("첫 번째 숫자를 입력하세요"))
# input2 = int(input("두 번째 숫자를 입력하세요"))

# total = input1 + input2
# print(f"두 수의 합은 {total}입니다.")

'Q6'
# user_input = input("저장할 내용을 입력하세요")
# f = open('test.txt', 'a')
# f.write(user_input)
# f.write("\n")
# f.close()

'Q7'
# f = open('test.txt', 'r')
# body = f.read()
# f.close()

# body = body.replace('java', 'Python')

# f = open('test.txt', 'w')
# f.write(body)
# f.close()

"""5장"""
'Q1'
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val

# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)

'Q2'
# class MaxLimitCalculator(Calculator):
    
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100
# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)
# print(cal.value)

'Q4'
a = [1, -2, 3, -5, 8, -3] 
print(list(filter(lambda x:x >= 0, a)))

'Q6'
b = [1, 2, 3, 4]
print(list(map(lambda x: x*3, b)))

'Q7'
c = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(c) + min(c))

'Q8'
print(round(17/3, 4))

'Q9'