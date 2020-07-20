import random
"""
names = ['Tome', 'Lily', 'Rose']
my_name = input('input you name : ')
if my_name in names:
    print('rename')
else:
    print('successfully insert you name!'.title())
    names.append(my_name)
print(names)

# 6.3.1 添
names.append(['Xi', 'Da'])
print(names)
# 6.4.0 删
names.pop(4)
# 6.3.2 添
names.extend(['Xi', 'Da'])
print(names)

# 6.7.1 while 遍历 names
i = 0
while i < len(names):
    print(names[i], end=' ')
    i += 1
print('\n')

# 6.7.2 for 遍历 names
for i in names:
    print(i, end=' ')
print('\n')


# 案例
'''
8个人，3个房间
'''
people = range(1, 9)
rooms = [[], [], []]
for i in people:
    num = random.randint(0, 2)
    rooms[num].append(i)  # 扔到随机一个
print(rooms)

# 打印每一个room
i = 1
for room in rooms:
    print(f'Room {i} have {len(room)} people: ')
    i += 1
    for j in room:
        print(j)

# tuple
t1 = (10, 9, 8, 7)
print(t1.index(9))
t2 = (10,)
print(type(t2))
t3 = (10)
print(type(t3))
t4 = (10, 9, 8, [7, 6])
t4[3][0] = 10
print(t4) 



# dictionary
dict1 = {'name': 'Tom', 'age': '18', 'gender': '男'}
# 8.2 添
dict1['id'] = '001'
print(dict1)
# 8.5.3
print(dict1.keys())
# 8.5.4
print(dict1.values())
# 8.5.5
print(dict1.items())
# 8.5.6 遍历keys
for key in dict1.keys():
    print(key)
# 8.5.7 遍历values
for value in dict1.values():
    print(value)
# 8.5.8 遍历items
for item in dict1.items():
    print(item)
# 8.5.9 遍历键值对
for key, value in dict1.items():
    print(f'{key} = {value}')


# set

# 9.1 创建集合
set1 = set('abcdef')
print(set1)

set2 = {100, 10, 1}

# 9.2 增
set2.add(1000)
print(set2)
set2.add(10)
print(set2)
set2.update([10, 1, 2, 3, 4])
print(set2)
# 9.3 删
set2.remove(10)
print(set2)
set2.discard(3)
print(set2)
pop_num = set2.pop()
print(pop_num)
print(set2)

# 9.4 查
print(4 in set2)

# 公共操作
# 10.1 '+'
str1 = 'aa'
str2 = 'bb'

list1 = ['a', 'b']
list2 = ['c', 'd']

tuple1 = (1, 2)
tuple2 = (3, 4)

print(str1+str2)
print(list1+list2)
print(tuple1+tuple2)

# 10.1 '*'
print(str1*10)
print(list1*5)
print(tuple1*5)

# 10.5 range()
print(range(10))
for i in range(0, 10, 5):
    print(i)

# 10.6 enumerate
for i in enumerate(tuple1,start=2):
    print(i)

# 10.7 str()\list()\tuple()\set()

print(list(str1))
print(tuple(str1))
print(set(str1))
print(str(list1))
print(tuple(list1))
print(set(list1))
print(str(tuple1))
print(list(tuple1))
print(set(tuple1))
print(str(set1))
print(list(set1))
print(tuple(set1))
"""
# 11.1 列表推导式
list1 = []
for i in range(10):
    list1.append(i)
print(list1)

# list1 = list2
list2 = [i for i in range(10)]
list3 = [i for i in range(10) if i % 2 == 0]
list4 = [(i, j) for i in range(2) for j in range(1, 3)]
print(list2)
print(list3)
print(list4)

# 11.2 元组推导式
tuple1 = tuple(i for i in range(10))
tuple2 = tuple(i for i in range(10) if i % 2 == 0)
tuple3 = tuple((i, j) for i in range(2) for j in range(1, 3))
print(tuple1)
print(tuple2)
print(tuple3)


# 11.3.1 字典推导式
dict1 = {i: i**2 for i in range(5)}
print(dict1)

# 11.3.2 两个列表合为一个字典
list01 = ['name', 'age', 'gender']
list02 = ['Tom', 20, 'man']  # len(list01) == len(list02)
dict2 = {list01[i]: list02[i] for i in range(len(list01))}
print(dict2)

# 11.3.3 提取字典
counts = {'MBP': 268, 'Hp': 125, 'Dell': 201, 'Iphone': 199}
dict3 = {key: value for key, value in counts.items() if value >= 200}
print(dict3)

# 11.4.1 集合推导式
list5 = [1, 1, 2]
set1 = {i ** 2 for i in list5}
print(set1)
