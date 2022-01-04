# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# 2 <= a,b,c <= 10000
# print((a+b)%c)
# print(((a%c)+(b+c))%c)
# print((a*b)%c)
# print((a%c)*(b%c)%c)

# a = input()
# b = input()
# a = int(a)
# b = str(b)
# print(a*int(b[2]))
# print(a*int(b[1]))
# print(a*int(b[0]))
# print(a*int(b))
 # 두 수 비교하기 문제
# a,b = input().split()
# a = int(a)
# b = int(b)
# -10000 <= a,b <=10000
# if a > b:
#     print(">")
# if a < b:
    # print("<")
# if a == b:
#     print("==")
 # 시험성적 문제
# a = int(input())
# 0 <= a <= 100
# if 90 <= a <= 100:
#     print("A")
# elif 80 <= a < 90:
#     print("B")
# elif 70 <= a < 80:
#     print("C")
# elif 60 <= a < 70:
#     print("D")
# else: 
#     print("F")
 # 윤년 문제
# year = int(input("연도를 입력 하십시오:"))
# 1 <= year <= 4000
# if (year%4 == 0) and (year%400 == 0):
#     print("1")
# elif (year%4 == 0) and (year%100 > 0):
#     print("1")
# else:
#     print("0")
#  사분면 고르기
# n1 = int(input())
# n2 = int(input())
# -1000 <= n1,n2 <= 1000 and n1,n2 != 0 
# if n1>0 and n2>0:
#     print("1")
# elif n1<0 and n2>0:
#     print("2")
# elif n1>0 and n2<0:
#     print("4")
# else:
#     print("3")

 # 알람시계 문제

# h,m = map(int, input().split())
# 0 <= h <= 23, 0 <= m <= 59

# if m >= 45:
#     print(h, m-45)
# elif 0 <= m < 45 and h != 0:
#     print(h-1, 60-(45-m))
# elif h == 0 and 0 <= m < 45:
#     print(23, 60-(45-m))

