# 更高效在实现代码重用
'''
# 12.1、12.2
print('login successfully')


def sel_func():
    print('1')
    print('2')
    print('3')


sel_func()


# 12.3参数


def add_num(a, b):
    result = a + b
    print(result)


add_num(10, 20)


# 12.4返回值


def buy():
    print('ok')
    return 'meat'


goods = buy()
print(goods)


def add_num2(a, b):
    """
    求和
    :param a:
    :param b:
    :return:
    """
    return a + b


sums = add_num2(1, 20)
print(sums)


# 12.5 函数嵌套


def test_B():
    print('This is B')


def test_A():
    print('A start')
    test_B()  # 引用函数
    print('A end')


test_A()


# 应用——画线


def print_line(i):
    print('-' * i)


def print_lines(j, k):
    """
    画不同长线
    :param j: 条数
    :param k: 长度
    :return: 无
    """
    num = 0
    while num < j:
        width = k[num]
        print_line(width)
        num += 1


print_lines(3, [10, 5, 13])


# 12.6 修改全局变量
glo_num = 0


def test1():
    global glo_num
    glo_num = 100


print(glo_num)  # 未调用，不修改
test1()   # 修改
print(glo_num)  # 已变



# 12.7 返回值做参数

def test1():
    return 50

def test2(num):
    print(num)

i = test1()
test2(i)



# 不定长参数
# 不定长位置参数
# 不定长关键字参数

def user_info(*args):
    print(args)

user_info('Tom', 18)

def user_info2(**kwargs):
    print(kwargs)

user_info2(name='Tom')

# 拆包
def return_num():
    return 100, 200

num1, num2 = return_num()
print(num1)
print(num2)




# 综合运用——学员管理系统,纯函数列表，没有存储功能

# 所有学员信息
info = []


# 显示界面，循环至6
def info_print():

    print('请选择功能：' + '-' * 19)
    print('1、添加学员', end='        ')
    print('2、删除学员')
    print('3、修改学员', end='        ')
    print('4、查询学员')
    print('5、显示所有学员', end='    ')
    print('6、退出系统')
    print('-' * 30)


# 添加学员信息
def add_info():
    """添加学员"""
    global info
    new_name = input('Name: ')
    new_id = input('ID : ')
    new_tel = input('Tel : ')
    for i in info:  # 不能if new_name in info.values() info还是list
        if new_name == i['Name']:
            print('已存在')
            return  # 退出函数
    else:

        info_dict = {'name'.title(): new_name, 'ID': new_id, 'Tel': new_tel}

        info.append(info_dict)
        print('添加学员成功！')
        print(info)

def del_info():
    """删除学员"""
    del_name = input('del_Name: '.title())
    global info
    for i in info:
        if del_name == i['Name']:
            info.remove(i)   # 不能用 del i 删不了，且无顺序
            print(info)
            print('删除成功')
        else:
            print('不存在')

def modify_info():
    """修改信息"""
    modify_name = input('modify_name:'.title())
    global info
    for i in info:
        if modify_name == i['Name']:
            # 改电话or改Id
            choose = int(input('modify_ID choose 1\nmodify_Tel choose 2\nmodify all choose 3\n: '))
            if choose == 1:
                mI = input('new_ID : ')
                i['ID'] = mI
            elif choose == 2:
                mT = input('new_Tel : ')
                i['Tel'] = mT
            else:
                mI = input('new_ID : ')
                i['ID'] = mI
                mT = input('new_Tel : ')
                i['Tel'] = mT
        else:
            print('不存在')
        break
    print(info)
# 输入功能序号并执行

def search_info():
    search_name = input('search_name:'.title())
    global info
    for i in info:
        if search_name == i['Name']:
            print('_'*30)
            print(f'Name is {i["Name"]}, ID is {i["ID"]},Tel is {i["Tel"]}')
        else:
            print('不存在')
        break

while True:
    info_print()
    user_num = int(input('请输入序号： '))
    # 循环不用global
    # 调用函数
    if user_num == 1:
        print('添加')
        add_info()
    elif user_num == 2:
        print('删除')
        del_info()
    elif user_num == 3:
        print('修改')
        modify_info()
    elif user_num == 4:
        print('查询')
        search_info()
    elif user_num == 5:
        print('显示所有')
        if not info:
            print([])
        else:
            for i in info:
                print(i)
    elif user_num == 6:
        print('退出系统')
        break
    else:
        print('输入有误,重新输入')




# 可变关键字参数
fn1 = lambda **kwargs: kwargs
print(fn1(name='python', age=18))

# lambda 运用1
fn1 = lambda a, b: a if a > b else b
print(fn1(100, 50))
print(fn1(10, 500))

# lambda 运用2
students = [{'name': 'Tom', 'age': 18},
            {'name': 'Ama', 'age': 20}]
students.sort(key=lambda x: x['name'])
print(students)
students.sort(key=lambda x: x['age'],reverse=True)
print(students)


# 高阶函数
print(abs(-10))
print(round(1.9))
def sum_num(a, b, f):
    return f(a)+f(b)
result = sum_num(10, -1, abs)
print(result)



import functools
# map()

list1 = [1, 2, 3, 4]

def func1(x):
    return x ** 2
result1 = map(func1, list1)
print(result1)
print(list(result1))

# reduce

def func2(a, b):
    return a + b

result2 = functools.reduce(func2, list1)
print(result2)

# filter

def func3(a):
    return a % 2 == 0

result3 = filter(func3, list1)
print(list(result3))

'''

# 递归
# 3以内累加和 = 3 + (2 以内累加和) = 3 + ( 2 + (1以内累加和 = 1//不再用函数——>出口))

def sum_nums(num):

    # 出口
    if num == 1:
        return 1
    return num + sum_nums(num-1)

sum_result = sum_nums(3)
print(sum_result)
