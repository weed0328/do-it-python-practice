"""1번 최소, 최대 문0제"""
# import sys
# n = (int, sys.stdin.readline())
# l = list(map(int, sys.stdin.readline().split()))
# print(f"{min(l)} {max(l)}")

"""2번 최댓값 문제"""
# """첫번째 방법"""
# import sys

# n = list()
# for i in range(9):
#     n.append(int(sys.stdin.readline()))
# print(f"{max(n)}")
# print(n.index(max(n)) + 1)

"""3번 숫자의 개수 문제"""
# import sys

# a = int(sys.stdin.readline())
# b = int(sys.stdin.readline())
# c = int(sys.stdin.readline())
# 100 <= a, b, c <= 1000
# mul = str(a*b*c)

# for i in range(10):
#     cnt = mul.count(str(i))
#     print(cnt)

"""4.나머지 문제"""
"""4-1 내장함수 set을 사용한 문제"""
# import sys

# num = []
# for _ in range(10):
#     n = int(sys.stdin.readline())
#     n_divi = n%42
#     num.append(n_divi)

# num_set = set(num)
# print(len(num))

"""4-2 내장함수를 사용하지 않은 문제"""
# import sys

# num = []
# for _ in range(10):
#     n = int(sys.stdin.readline())
#     n_divi = n%42
#     num.append(n_divi)

# count_list = [0 for i in range(42)]
# for i in range(10):
#     for j in range(42):
#         if num[i] == j:
#             count_list[j] += 1

# count_num = 0
# for i in range(42):
#     if count_list[i] != 0:
#         count_num += 1

# print(count_num) 

"""이상적인 답안 씨발ㅠㅠㅠ"""
# A=set()
# for i in range(10):
#     n = int(input())
#     A.add(n%42)
# print(len(A))

"""5.평균 문제"""
# import sys

# n = int(sys.stdin.readline())
# scores = list(map(int, sys.stdin.readline().split()))
# fn = []

# for i in range(n):
#     fn.append(scores[i]/max(scores)*100)

# print(sum(fn)/len(fn))

"""6.OX 퀴즈 문제"""
# import sys

# n = int(sys.stdin.readline())

# for i in range(n):
#     OX = sys.stdin.readline()
#     count_O = 0
#     total = 0
#     for j in OX:
#         if j == "O":
#             count_O += 1
#             total += count_O
#         else:
#             count_O = 0
#     print(total)

"""4344번 평균은 넘겠지 문제"""
# import sys

# N = int(sys.stdin.readline())

# for i in range(0,N):
#     count = 0
#     sum_scores = 0
#     scores = list(map(int, sys.stdin.readline().split()))
#     for j in range(1, scores[0] + 1):
#         sum_scores = sum_scores + scores[j]
#     avg = sum_scores/scores[0] 
    
#     for y in range(1, scores[0] + 1):
#         if scores[y] > avg:
#             count = count + 1
#         else:
#             pass
#     answer = "{:0,.3f}".format((count/scores[0])*100)
#     print(f"{answer}%")

