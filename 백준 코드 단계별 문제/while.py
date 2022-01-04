# While 예제 1번
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)
    
# while 예제 2번
# import sys

# while True:
#     try:
#         a, b = map(int, sys.stdin.readline().split())
#         print(a+b)
#     except:
#         print("임동락 병신")

# while 더하기 사이클 문제
# n = int(input())
# a = n
# i = 0
# while True:
#     n1 = n // 10
#     n2 = n % 10
#     n3 = n1 + n2
#     n4 = n3%10
#     n = int(str(n2) + str(n4))
#     i += 1
#     if n == a:
#         break
# print(i)

print('=' * 50)
print("my program")
print('=' * 50)