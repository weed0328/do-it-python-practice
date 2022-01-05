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

# '''if문 한줄로 작성하기'''
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

# '''while문!!!!!!!!!!!!!!!!'''
# treeHit = 0
# while treeHit < 10:
#     treeHit += 1
#     print(f'나무를 {treeHit}번 찍었습니다.')
#     if treeHit == 10: print("나무 넘어갑니다. 다치기 싫으면 비키세요")

# '''문제 맞출때까지 문제 반복하기'''
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
from functools import total_ordering


coffee = 10
price = 300
total_price = 0
while price:
    print('300원 넣으셨군요! 믹스커피 한 잔 나갑니다.')
    coffee -= 1
    total_price = total_price + price
    print(f'남은 커피는 {coffee}잔 입니다.')
    if coffee == 0:
        print(f"커피가 모두 소진되었습니다.\n남은 커피{coffee}잔\n 총 수익:{total_price}")
        break