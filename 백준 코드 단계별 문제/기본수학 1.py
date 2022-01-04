"""손익분기점"""
# a, b, c = map(int, input().split())


# if b >= c:
#     print(-1)

# elif b < c:
#     x = (a // (c - b)) + 1
#     print(x)

'''벌집'''
'''오답!'''
# N = int(input())
# n = N//6
# s = 1 + (n-1)*6
# import sys
# x= int(sys.stdin.readline())
# l =[]
# for i in range(1, 1000000000):
#     t = ((i*(2 + (i-1)*6))//2)
#     if t < x:
#         l.append(t)
#     elif t > x:
#         break
# print(l)

# for j in range(100000):
#     if l[j] < x <= l[j+1]:
#         print(j+1)
#         break
#     else:
#         pass
''' 정답!! '''
# N = int(input())

# a = 1
# b = 1
# while N > b:
#     if N > a:
#         b = b + 6*a
#         a += 1
# print(a)

"""분수"""
# n = int(input())
# 0
# num = 0
# sum = 0
# while n > sum:
#     num += 1
#     sum = sum + num # 1 3 6 10

# a = sum - n

# if num % 2 == 0:
#     boonza = num - a
#     boonmo = a + 1

# elif num % 2 != 0:
#     boonza = a + 1
#     boonmo = num -a

# print(f"{boonza}/{boonmo}")


"""달팽이"""
import sys ; import math
A, B, V = map(int, sys.stdin.readline().split())

C = A-B
n = V-A
a = 1
y = 1
while  y <= n:
    y = C*a
    a = a + 1
print(a-1)





