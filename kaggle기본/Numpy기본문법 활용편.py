import numpy as np
print(np.__version__)
temp = [i for i in range(1, 11)]
temp_array = np.array(temp) # 배열로 변환

print(type(temp_array))
print(len(temp_array))
print(temp_array[0])
print(temp_array[6])
print(temp_array[-1]); print(temp_array[9])

'''평균값을 구하는 mean메서드'''
print(np.mean(temp_array))

"""사칙연산"""
math_scores = [90, 80, 88, 75, 85]
english_scores = [90, 100, 88, 80, 85]

#Total
print(math_scores + english_scores) # 이렇게 리스트 덧셈을 실시하면 두개의 리스트가 합쳐짐

math_array = np.array(math_scores)
english_array = np.array(english_scores)

total_scores = math_array + english_array  #각 요소의 합이 반환됨
print(total_scores)
#그렇다면 일반적인 리스트와 배열을 합치면?
print(math_scores + english_array) #기본적으로 배열의 형태로 연산이 됨
 #그러나 차원이 다르다던가 요소의 갯수 즉 크기가 다르면 오류가 남
print(np.min(total_scores)) #최소값
print(np.max(total_scores)) #최댓값

"""배열의 생성"""
'''0차원'''
temp_arr = np.array(30)
print(type(temp_arr))
print(temp_arr.shape) #비어있음 즉, 숫자 하나는 0차원이라는 뜻 에러가 아님!

'''1차원'''
temp_arr1 = np.array([1, 2, 3, 4])
print(type(temp_arr1))
print(temp_arr1.shape) #튜플로 반환되기 때문에 ,다음 빈칸 생성

'''2차원'''
temp_arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(temp_arr2)
print(type(temp_arr2))
print(temp_arr2.shape) #2차원 2행 3열이라는 뜻

'''3차원'''
temp_arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(temp_arr3)
print(type(temp_arr3))
print(temp_arr3.shape) #2행 3열짜리 배열이 두 개 있다.

temp_last = np.array([1, 2, 3, 4], ndmin = 3) #ndmin을 통해 애초에 차원의 크기를 설정 가능
print(temp_last)
print(temp_last.shape)

