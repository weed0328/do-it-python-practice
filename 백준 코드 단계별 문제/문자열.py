"""1번 아스키 코드"""
# print(ord(input()))

"""2번 숫자의 합"""
""" 2-1 함수를 쓰지 않은 것 """
# n = int(input())
# a = str(input())
# y = 0
# for i in a:
#     y = y + int(i)
# print(y)

"""3번 알파벳 찾기"""
# S = input()
# alp = 'abcdefghijklmnopqrstuvwxyz'
# for i in alp:
#     print(S.find(i),end=' ')

"""문자열 반복"""
# T = int(input())
# 1 <= T <= 1000
# for _ in range(T):
#     R, S = input().split()
#     P = ""
#     1 <= int(R) <= 8
#     for i in str(S):
#         P = P + int(R)* i
#     print(P)
'''문자열 또한 리스트처럼 빈 문자열을 생성 가능하다.'''

"""단어공부""" '''깅장히 어려웠던 문제 다시풀어도 못풀듯..?'''
# word = input().upper()      # MISSISSIPI,  / BAAA
# word2 = list(set(word))      #M, I, S, P  / B, A 
# list = []
# for i in word2:
    # list.append(word.count(i))  # list = [1, 4, 4, 1] / [1, 3]
# if list.count(max(list)) >= 2:
    # print("?")
# else:
#     print(word2[list.index(max(list))]) 

"""단어의 개수"""
# word = input()
# word_list = word.split()
# print(len(word_list))

"""상수 문제"""
# A, B = map(str, input().split())
# l = [];l2 = []
#for i in A:
#    l.append(i)
# l.reverse()        # reverse함수는 리스트를 역순으로 나타내준다!
# l = ''.join(l)     # join 함수는 리스트를 문자열로 변환해준다! point!
# int(l)
# for j in B:
#     l2.append(j)
# l2.reverse() ; 
# l2 = ''.join(l2) 
# int(l2)
# if l > l2:
#     print(l)
# elif l < l2:
#     print(l2)
# else:
#     pass

"""다이얼 문제"""
# Number = {'ABC': 3, 'DEF': 4, 'GHI' : 5, 'JKL': 6, 'MNO':7, 'PQRS':8, 'TUV': 9, 'WXYZ':10}
# alp = list(input())
# a = []

# for i in Number:
#     for j in alp:
#         if j in i:
#             a.append(Number[i])
#         else:
#             pass

# answer = sum(a)
# print(answer)
0
"""크로아티아 알파벳"""
'''replace 함수로 문자열 내 다양한 길이ㅡㄹ 가진 부분을 하나의 문자로 치환 후 len쳐줌'''
# cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = str(input())

# for i in cro:
#     word = word.replace(i, 'a')
# print(len(word))

"""그룹단어 체커"""
'''실패 '''
# N = int(input())
# check = 0
# word = [str(input()) for _ in range(N)]

# for i in range(N):             
#     a = list((word[N-1]))
#     b = len(a)
#     c = set(a)
#     if len(c) == len(a):
#         check = check + 1
#     elif len(c) != len(a):
#         for j in range(len(a)-1):
#             if a[j] == a[j+1]:
#                 b = b - 1
#             elif a[j] != a[j+1]:
#                 pass
#             elif j+1 < len(a):
#                 break
#         if b == len(c):
#             check = check + 1
#         elif b != len(c):
#             pass
#     else:
#         pass
# print(check)


"""시발...ㅠㅠㅠ"""   '''정답'''
# N = int(input())
# ans = N

# for i in range(N):
#     a = list(input())      
#     b = set()
#     for j in range(len(a) - 1):
#         if a[j] != a[j+1] and a[j+1] in b:
#             ans = ans - 1
#             break
#         else:
#             b.add(a[j])

# print(ans)
