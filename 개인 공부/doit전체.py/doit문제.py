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
# ave = a
# print(ave)

# '''doit Q3'''
# pin = "000328-1068234"
# yyyymmdd = pin[:6]
# num = pin[7:]
# print(yyyymmdd)
# print(num)

# '''doit Q3'''
# a = "a:b:c:d"
# b = a.replace(":", "#")
# print(b)

# '''doit Q4'''
# a = [1, 3, 5, 4, 2]
# a.sort()
# a.reverse()
# print(a)

# '''doit Q5'''
# a = ['Life', 'is', 'too', 'short']
# result = " ".join(a)
# print(result)

# '''doit Q8'''
# a = 1, 2, 3
# a = a + (4,)
# print(a)

# '''doit Q9'''
# ''' 딕셔너리의 키값에는 변하는 값인 리스트를 집어넣을 수가 없다.'''

# '''doit Q10'''
# a = {'A':90, 'B':80, 'C':70}
# result = a.pop('B')
# print(a)
# print(result)

# '''doit Q11'''
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = set(a)
# b = list(aSet)
# print(b)

'''doit Q12'''
a = b = [1, 2, 3]
a[1] = 4
print(b)