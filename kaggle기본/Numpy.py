from tracemalloc import stop
import numpy as np
# A = [1, 2, 3]
# B = [4, 5, 6]

# np_A = np.array(A)
# np_B = np.array(B)

# a = np_A / np_B ** 2
# print(a)
"""Numpy 기본 문법"""
'''arange'''
# arrange_array = np.arange(5) #기본함수 중 Range함수와 비슷하며, 숫자를 입력할 때는 0부터 숫자의 크기만큼 1차원 배열이 만들어진다.
# print(arrange_array)

# arrange_array1 = np.arange(1, 9, 3)
# print(arrange_array1) #range함수처럼 1부터 9까지 3씩 커짐

'''zeroes, ones'''
# zeros_array = np.zeros((3, 2)) #zeros 함수는 설정한 행열에 0을 집어넣어 버린다.
# print(zeros_array)
# print("Data type is:", zeros_array.dtype)
# print("Data shape is:", zeros_array.shape)

# ones_array = np.ones((3,4), dtype = 'int32')# type을 미리 지정해 놓으면 강제로 지정된다. 여기서는 int32로 고정됨
# print(ones_array)                           #마찮가지로 1이 들어간다.
# print("Data type is:", ones_array.dtype)
# print("Data shape is:", ones_array.shape)

'''reshape''', '''<-- 행과 열을 바꾸어주는 함수'''
# temp_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
# print(temp_arr)

# new_arr = temp_arr.reshape(2, -1) # 특정 차원에서 행은 2로 고정한 상태로 열은 사이즈에 맞도록 자동정렬해준다는 뜻 <-- -1의 의미
# print(new_arr)
# new_arr2 = temp_arr.reshape(4, -1)
# print(new_arr2)

# after_reshape = ones_array.reshape(6, 2)
# print(after_reshape)
# print("Data shape is:", after_reshape.shape)

#단, reshape는 Size가 동일한 상황에서 만 변경이 가능하다. 밑의 식은 에러반환
# after_reshape2 = ones_array.reshape(5,3) # ones_array는 12개의 요소를 가지고 있는데 바꾸려는 배열은 15개의 요소를 필요로 함
# print(after_reshape2)

'''reshape는 1차원에서3차원으로도 변경 가능'''
# after_reshape3 = ones_array.reshape(2, 3, 2) #
# print(after_reshape3)
# print("Data shape is:", after_reshape3.shape)

'''-1은 다른차원을 자동으로 계산한다.'''
# after_reshape4 = ones_array.reshape(-1, 6)
# print("reshape(-1, 6)? \n")
# print(after_reshape4)

# after_reshape5 = ones_array.reshape(3, -1)
# print("reshape(3, -1)? \n")
# print(after_reshape5)

"""Numpy에서의 인덱싱과 슬라이싱"""
'''특정한 데이터를 찾는 것을 인덱싱, 데이터를 따로 추출해내는 것은 슬라이싱이라 한다.'''
my_array = np.arange(start=0, stop=4)
my_array = np.arange(0, 4)
print(my_array)
print(my_array[0:3])

#구구단 3단 숫자들이 모인 2차원 배열
my_array2 = np.arange(3, 30, 3)
my_array2 = my_array2.reshape(3, 3)
print(my_array2)

print(my_array2[0:2, 0:2]) #0~1번째 행과 열만 불러온 것 
print(my_array2[1:3, :])   #1~2번째 행과 모든 열을 불러온 것 : 앞뒤 생략하면 싹 다 포함
print(my_array2[:,:])

"""Numpy 정렬"""
'''np.sort()함수는 원래의 배열은 그대로 놔둔채 정렬의 결과를 복사본으로 반환한다.'''
'''np.sort()함수는 오름차순으로 자동정렬'''
height_arr = np.array([174, 165, 180, 182, 168])
sorted_height_arr = np.sort(height_arr)
print('height_matrix:', height_arr)
print("np.sort() matrix:", sorted_height_arr) #오름차순

'''내림차순으로 정렬하고 싶다면'''
desc_sorted_height_arr = np.sort(height_arr)[::-1] #[::-1]을 붙이면 내림차순 정렬이 된다.
print('np.sort()[::1]:', desc_sorted_height_arr)

'''argsort'''
'''numpy.argsort()함수는 지정된 축을 따라 데이터 인덱스의 배열을
반환하도록 지정된 종류의 정렬을 사용해 입력 배열에서 간접정렬을 수행한다.'''
five = np.array([10, 5, 15, 20])
fives_order = five.argsort()
print("The original data:", five)
print("The argsort():", fives_order)
print("The asending:", five[fives_order])