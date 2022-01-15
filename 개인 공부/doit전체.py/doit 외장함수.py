"""외장함수"""

#pickle 객체의 형태를 그랟로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
# import pickle

# f = open("test.txt", 'wb')  
# data = {1: 'python', 2: 'you need'}
# pickle.dump(data, f) #pickle의 dump를 사용하여 data 딕셔너리 형태 그대로를 파일에 저장
# f.close()

# f = open("test.txt", 'rb')
# data = pickle.load(f)    #pickle.dump로 저장한 파일을 pickle.road로 불러옴
# print(data)
# {1:'python', 2:'you need'}

#OS 환경변수나 디렉터리 파일등의 OS자원을 제어 할 수 있게 해주는 모듈
import os
print(os.environ) # 내 시스템의 환경변수를 알고 싶을때 사용한다.
print(os.environ['PATH'])

# os.chdir("C:\WINDOWS") <-- 현재 디렉터리의 위치를 변경해줌
print(os.getcwd())      #<-- 현재 디렉터리의 위치를 알려줌

os.system("dir") # <-- 시스템 명령어 호출하기