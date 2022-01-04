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
# ave = a//3
# print(ave)

'''doit Q2'''
pin = "000328-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

