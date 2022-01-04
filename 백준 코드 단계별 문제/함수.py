"""정수 N개의 합"""
# def solve(a):
#     return(sum(a))

"""셀프넘버"""

# def selfnumber():
#     all_number = set(range(1,10001))
#     not_self = set()
    
#     for i in range(1, 10001):
#         sum  = 0
#         mun = list(str(i))
#         for j in mun:
#             sum += int(j)
#         not_self.add(sum + i)

#     self_num = sorted(all_number - not_self)
#     for t in self_num:
#         print(t)

# selfnumber()

"""3번, 한수 문제"""
"""하다가 실패 밑에서 다시 도전"""
# import sys

# def han_su():
#     total = 0
#     a = []
#     n = int(sys.stdin.readline())
#     if n < 100:
#         print(n)
#     elif 1000 > n >= 100:
#         for i in range(100, n+1):
#             for j in str(i):
#                 a.append(int(j))
#                 if a[2] - a[1] == a[1] - a[0]:
#                     total += 1
#                 a.clear()
#     else:
#         pass
#     print(99 + total)
# han_su()

"""두번째 도전"""
# def han_su(n):
#     a = 0    
#     if 1 <= n < 100:
#         return n
#     else:
#         for i in range(100, n+1):
#             hund = i//100
#             ten = ((i%100)//10)
#             one = (i%10)
#             if (hund - ten) == (ten - one):
#                 a += 1    
#     return(99 + a)

# num = int(input())
# print(han_su(num))
"""ㅠㅠ 다풀었듀ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ"""
