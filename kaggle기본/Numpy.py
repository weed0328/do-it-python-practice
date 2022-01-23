import numpy as np
# A = [1, 2, 3]
# B = [4, 5, 6]

# np_A = np.array(A)
# np_B = np.array(B)

# a = np_A / np_B ** 2
# print(a)
"""Numpy 기본 문법"""
'''arange'''
arrange_array = np.arange(5) #기본함수 중 Range함수와 비슷하며, 숫자를 입력할 때는 0부터 숫자의 크기만큼 1차원 배열이 만들어진다.
print(arrange_array)

arrange_array1 = np.arange(1, 9, 3)
print(arrange_array1) #range함수처럼 1부터 9까지 3씩 커짐

'''zeroes, ones'''
zeros_array = np.zeros((3, 2)) #zeros 함수는 설정한 행열에 0을 집어넣어 버린다.
print(zeros_array)
print("Data type is:", zeros_array.dtype)
print("Data shape is:", zeros_array.shape)

ones_array = np.ones((3,4), dtype = 'int32')# type을 미리 지정해 놓으면 강제로 지정된다.
print(ones_array)                           #마찮가지로 1이 들어간다.
print("Data type is:", ones_array.dtype)
print("Data shape is:", ones_array.shape)

'''reshape''', '''<-- 행과 열을 바꾸어주는 함수'''
temp_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
print(temp_arr)

new_arr = temp_arr.reshape(2, -1) # 특정 차원에서 행은 2로 고정한 상태로 열은 사이즈에 맞도록 자동정렬해준다는 뜻 <-- -1의 의미
print(new_arr)
new_arr2 = temp_arr.reshape(4, -1)
print(new_arr2)

after_reshape = ones_array.reshape(6, 2)
print(after_reshape)
print("Data shape is:", after_reshape.shape)

#단, reshape는 Size가 동일한 상황에서 만 변경이 가능하다. 밑의 식은 에러반환
# after_reshape2 = ones_array.reshape(5,3) 
# print(after_reshape2)

'''reshape는 1차원에서3차원으로도 변경 가능'''
after_reshape3 = ones_array.reshape(2, 3, 2)
print(after_reshape3)
print("Data shape is:", after_reshape3.shape)
