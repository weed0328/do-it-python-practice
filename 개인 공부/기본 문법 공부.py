# insects = ['cockroach', 'dragonfly', 'mantis']
# insects.pop(0) # 인덱스 번호 0번
# print(insects)

from collections import deque
list = deque([1, 2, 3, 4,5])
list.rotate(-2)
print(list)