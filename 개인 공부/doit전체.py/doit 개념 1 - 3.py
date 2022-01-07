'''if문!!!!!!!!!!!!!!!'''
# money = 2000
# card = True
# if money >= 3000 or card:
#     print('타고가')
# else:
#     print('ㅉㅉ 그지 쉑 걸어가라')

# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     print('타고 가')
# else:
#     print('걸어가라')

# pocket = ['paper', 'cellphone']
# card = True
# if 'money' in pocket:
#     print('타고 가')
# elif card:
#     print('타고 가')
# else:
#     print('기어가')

'''if문 한줄로 작성하기'''
# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket: print('돈을 꺼내라')
# else: print('카드를 꺼내라')

'''파이썬의 조건부표현식'''
'''조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우'''
# score = int(input())
# if score >= 60:
#     message = "success"
# else:
#     message = "failure"

# score = 90
# message = "success" if score >= 60 else "failure"

'''while문!!!!!!!!!!!!!!!!'''
# treeHit = 0
# while treeHit < 10:
#     treeHit += 1
#     print(f'나무를 {treeHit}번 찍었습니다.')
#     if treeHit == 10: print("나무 넘어갑니다. 다치기 싫으면 비키세요")

'''문제 맞출때까지 문제 반복하기'''
# import sys
# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit

# Enter number: """

# number = 0
# while number != 4:
#     print(prompt)
#     number = int(sys.stdin.readline())

'''커피 뽑는 기계!'''
# coffee = 10
# price = 300
# total_price = 0
# while price:
#     print('300원 넣으셨군요! 믹스커피 한 잔 나갑니다.')
#     coffee -= 1
#     total_price = total_price + price
#     print(f'남은 커피는 {coffee}잔 입니다.')
#     if coffee == 0:
#         print(f"커피가 모두 소진되었습니다.\n남은 커피{coffee}잔\n총 수익:{total_price}")
#         break

'''실재 자판기 처럼!!'''
# import sys
# coffee = 10

# while True:
#     price = int(sys.stdin.readline())
#     if coffee == 0:
#         break
#     elif price == 300:
#         print("커피가 나왔습니다.")
#         coffee -= 1
#         print(f"남은 커피는{coffee}잔 입니다.")
#     elif price > 300:
#         remain = price - 300
#         print(f"커피가 나왔습니다. 거스돈은{remain}원 입니다.")
#         coffee -= 1
#         print(f"남은 커피는{coffee}잔 입니다.")
#     elif 0 <= price < 300:
#         remain2 = 300 - price
#         print(f"금액이 부족합니다. {price}원을 반환합니다.")
#     else:
#         pass
'''while문의 맨 처음으로 돌아가기'''
# a = 0
# while a < 10:
#     a += 1
#     if a % 2 == 0: continue
#     print(a)

'''for문 포문포문!'''
# test_list = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in test_list: # test_list 리스트 값이 튜플이기 때문에 자동으로 first last에 대입
#     print(first + last)

'''총 다섯명의 학생이 시험을 보았는데 시험점수가 60점이넘으면 합격이고
그렇지 않으면 불합격읻. 합격인지 불합격인지 결과를 도출하라'''

# import sys
# students = []
# for i in range(5):
#     a = int(sys.stdin.readline())
#     students.append(a)

# s_number = 0

# for i in students:
#     s_number += 1
#     if i >= 60: print(f"{s_number}번 학생은 합격입니다.")
#     else:       print(f"{s_number}번 학생은 불합격입니다. 짐 싸세요.")

# students = [90, 25, 67, 45, 80]
# s_number = 0

# for i in students:
#     s_number += 1
#     if i < 60: continue
#     print(f"{s_number}번 학생 축하해요 당신은 합격입니다.")

# students = [90, 25, 67, 45, 80]

# for a in range(len(students)):
#     if students[a] < 60: continue
#     print(f"{a+1}번 학생 축하합니다. 당신은 합격입니다.")

"""구구단!!"""
# for i in range(2, 10):
#     for j in range(1, 1000):
#         print(i*j, end=" ")
#     print('')

'''리스트 내포 사용하기'''
# a = [1,2,3,4]
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)
"""기본적인 리스트 내포 문법""" '--->'  '''[항목표현식 for 항목 in 반복가능객체 if 조건]'''

'''for문과 if문 여러개를 한꺼번에 사용하는 것도 가능'''
'''구구단의 모든 결과를 한 리스트에 담고 싶을 경우'''
# result = [i*j for i in range(2, 11)
#             for j in range(1, 11)]
# print(result)

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
        i += i
print(result)