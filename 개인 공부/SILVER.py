'''V - 다리놓기'''
# import sys

# def factorial(n):
#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num


# test_num = int(sys.stdin.readline())

# for j in range(test_num):
#     N, M = map(int, sys.stdin.readline().split())
#     0 < N <= M < 30
#     total_site = factorial(M) // (factorial(N)*factorial(M - N))
#     print(total_site)

"""팩토리얼을 어덯게 나타낼가 하다가 하나의 함수로 만들어놓고
푼 문제, 나중에 알고보니 import math 해놓고 내장함수 쓰면 되는걸
알았다."""

"""V - 약수 문제"""
# n = int(input())
# divisor = list(map(int, input().split()))

# n1 = min(divisor)
# n2 = max(divisor)

# print(n1 * n2)

'''한줄에 여러가지 깂 입력 받는거 이제는 외워야 한다.'''

"""V - 좋은구간"""
# import sys

# L = int(sys.stdin.readline())
# 1 <= L <= 50 
# S = [0] + sorted(list(map(int, sys.stdin.readline().split())))  # 이 부분에서 0 추가
# min(S) >= 1
# max(S) <= 1000

# n = int(sys.stdin.readline())
# min(S) <= n <= max(S)

# for i in range(0, L):
#     if S[i] < n < S[i+1]:
#         print((n - S[i]) * (S[i+1] - (n)) - 1)
#     elif S[i] == n:
#         print(0)
#     else:
#         pass
""" 계속 채점 중 20%에서 틀렸다고 하길래 찾아봤더니 하나의 반례를 생각해내지 못했다.;
바로 정수집합의 원소가 하나만 주어지는 상황에서 틀렸던 것이다. 그래서;
집합 S에 0을 하나 추가해줌으로써 원소가 하나만 입력되더라도 0과;
그 값 사이의 범위가 나오도록 만들었다. 그랬더니 정답!!"""

"""V - 요세푸스 문제"""
'''실패버전'''
# N, K = map(int,input().split())
# T_list = []
# yo_list = [i for i in range(1, N+1)]
# for _ in range(N):
#     if K <= N:
#         T_list.append(yo_list[K-1])
#         K = K+K
#         N = N-1
#     elif K > N:
#         T_list.append(yo_list[K-N-1])
#         K = K - N + K
#         N = N - 1
#     elif len(T_list) == N:
#         print(T_list)

"""재도전""" '''deque 선형 자료구조 다시 정리하기 은근 유용함!! 리스트와 비교'''
# from collections import deque
# N, K = map(int,input().split())
# list = []
# yo_que = deque(range(1, N+1))
# K = K-1
# while len(yo_que) >= 1:
#     yo_que.rotate(-K)
#     list.append(yo_que[0])
#     yo_que.popleft()

# print('<'+', '.join(map(str, list))+'>')
'''리스트에 str 및 int 씌워줄때는 제발!!! 꼭!!!!! map함수 사용해라!!!!!!!!!!!!!!!!!!!!'''

"""V - 단어 정렬"""
'''첫 번째 도전 실패'''
# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# word_num = []
# word = []
# answer = []
# for _ in range(N):      # 길이가 짧은 것부터 순서대로 정렬하는 식
#     a = str(sys.stdin.readline().strip())
#     a = str(len(a)) + a
#     word_num.append(a)
# word_num.sort()

# for i in range(N):     # 리스트 내 요소들의 크기를 없애고 사전 순으로 정렬하는 식
#     l = deque(word_num[i])   # 내가 바보였다. 문자열 인자의 길이가 길면 앞에 있는 숫자 하나만 빼줘서는 안됐던것
#     l.popleft()
#     l = ''.join(l)
#     word.append(l)
# sorted(word)

# for j in word:         # 리스트 내 중복된 요소 없애주기
#     if j not in answer:
#         answer.append(j)
#     else:
#         pass
# for y in answer:       
#     print(y)

'''두 번째 도전 성공'''
# n = int(input())       #문자개수 입력

# words = [input() for i in range(n)] #문자열 리스트 생성

# words = set(words)     #중복제거
# rwords = list(words)   

# rwords.sort()           # 사전순으로 정렬
# rwords.sort(key = len)  # 길이 순으로 정렬 << 몰랐던 사실

# for i in rwords:         #출력!
#     print(i)

"""V - 쉽게푸는 문제"""
'''실패'''
# A, B = map(int, input().split())
# l = [1]
# a = 1
# for j in range(1, 1001):
#     a = a + j
#     l.append(a)

# for i in range(1, len(a)):
#     if l[i] <= A < l[i+1]:
#         num1 = l[i+1] - A
#         sum1 = l[i]*num1
#         a = l[i + 1]
#     if l[i] <= B < l[i+1]:
#         if 0 == B - l[i]:
#             sum2 = l[i]
#         else:
#             num2 = B - l[i]
#             sum2 = num2*l[i]
#         b = l[i]
'''성공'''
# A, B = map(int, input().split())

# l = []

# for i in range(1,46):
#     l += [i] * i

# print(sum(l[A-1:B]))
'''귽이'''