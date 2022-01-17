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
# import os
# print(os.environ) # 내 시스템의 환경변수를 알고 싶을때 사용한다.
# print(os.environ['PATH'])

# # os.chdir("C:\WINDOWS") <-- 현재 디렉터리의 위치를 변경해줌
# print(os.getcwd())      #<-- 현재 디렉터리의 위치를 알려줌

# os.system("dir") # <-- 시스템 명령어 호출하기

# f = os.popen("dir") #os.popen은 시스템 명령어를 실행한 결괏값을 읽기모드 형태의 파일 객체로 돌려줌
# print(f.read())

# """기타 유용한 os함수"""
# os.mkdir('디렉터리') #디렉터리를 생성한다.
# os.rmdir('디렉터리') #디렉터리를 삭제한다. 단, 디렉터리가 비어있어야 가능하다.
# os.unlink('파일 이름') # 파일을 지운다
# os.rename('src', 'dst') #src라는 이름의 파일을 dst라는 이름으로 바꾼다.

'''shutle''' #파일을 복사해주는 파이썬의 모듈
# import shutil
# shutil.copy('src.txt', 'dst.txt') #src라는 파일을 dst로 복사한다. 만약 dst가 디렉터리라면 src라는 파일이름으로 dst디렉터리에 복사하고 동일한 파일이름인 경우에는 덮어쓴다.

'''glob'''
#glob 모듈은 디렉터리 안에 있는 파일들을 읽어서 돌려준다. *,?등 메타문자를 써서 원하는 파일만 읽을 수 있음.
# import glob
# glob.glob("c:/개인공부/doit*") # c:/개인공부 디렉터리 안에 있는 파일들 중 doit으로 시작하는 파일들을 모두 찾아서 읽어준다.

'''tempfile''' #파일을 임시로 만들어서 사용하는 함수
# import tempfile
# filename = tempfile.mkstemp() # tempfile.mkstemp()는 중복되지 않는 임시파일의 이름을 무작위로 만들어서 돌려준다.

# f = tempfile.TemporaryFile() #tempfile.TemporaryFile()은 임시 저장공간으로 사용할 파일객체를 돌려준다. 이 파일은 기본적으로 wb모드를 갖으며 f.close가 호출되는 순간 사라진다
# f.close()

"""time"""
import time
print(time.time()) #1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초단위로 알려줌

print(time.localtime(time.time()))  #시간을 복잡하게 보여줌
print(time.asctime(time.localtime(time.time())))  #시간을 간략하게 보여줌
print(time.ctime()) #바로 윗줄 간략하게 요약

#time.strftime('출력할 형식 포멧코드', time.localtime(time.time()))
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time()))) #포멧 코드는 책에서...

# for i in range(10):
#     print(i)
#     time.sleep(1) # time.sleep 주로 루프안에서 사용하는 함수로 일정한 시간간격을 두고 루프 실행 1초간격으로 0부터 9까지 출력하라는 소리

"""calender""" #파이썬에서 달력을 볼 수 있게 해주는 함수
import calendar
# print(calendar.calendar(2022))
print(calendar.prmonth(2022, 2)) # 해당연도의 해당 월의 달력을 보여준다.
print(calendar.weekday(2022, 12, 31)) #해당날짜가 무슨 요일인지 풀력한다. 0부터 6까지 월부터 일
print(calendar.monthrange(2022, 1)) #입력받은 달의 1일이 무슨 요일인지와 며칠까지 있는지 보여준다.

"""random""" #난수를 발생시키는 모듈이다.
import random
print(random.random()) # 0.0에거 1.0 가이의 실수중에서 난수값을 돌려주는 예
print(random.randint(1, 10)) #1부터 10까지의 정수 중에서 난수값 반환

def random_pop(data):                            #data 리스트 안에 있는 요소들중 무작위로 아무거나 꺼내서 반환한다. 꺼낸 요소는 pop에 의해 사라짐
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ =="__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))


def random_popp(data):
    number = random.choice(data)   #unmber.choice를 사용하면 입력받은 리스트에서 무작위로 하나를 선택하여 돌려줌
    data.remove(number)
    return number


data = [1, 2, 3, 4, 5]
random.shuffle(data) #random.shuffle은 리스트를 무작위로 섞어준다.
print(data)

"""webbrowser"""
import webbrowser
webbrowser.open("http://google.com")