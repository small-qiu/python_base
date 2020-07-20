class Washer(object):

    def wash(self):
        print('能洗衣服')
        print(self)

    def __str__(self):
        return '海尔'


# haier1 = Washer()
# print(haier1)   # 内存地址，用__str__后不再返回地址，而是return后的文字
# haier1.wash()
#
# haier2 = Washer()
# print(haier2)
# haier2.wash()


# 应用

# 应用
class SweetPotato(object):

    def __init__(self):

        self.cook_time = 0
        self.cook_static = '生的'
        self.condiments = []

    def cook(self, time):
        """根据时间判断状态"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time <8:
            self.cook_static = '熟了'
        elif 8 < self.cook_time:
            self.cook_static = '糊了'

    def add_condiments(self, condiments):
        self.condiments.append(condiments)

    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}, {self.cook_static},调理有{self.condiments}'


# digua1 = SweetPotato()
# print(digua1)
# # print(digua1.cook_time)
# digua1.cook(2)    # 用方法修改self.cook_time 并储存，用下次调用
# print(digua1)
# digua1.add_condiments('辣椒')
# # print(digua1.cook_time)
# digua1.cook(3)
# print(digua1)

class Furniture(object):

    def __init__(self, name, area):

        # 家具名称
        self.name = name
        self.area = area


class House(object):

    def __init__(self, address, area, ):

        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'房屋地理位置在{self.address},房屋的面积为{self.area},剩余面积为{self.free_area},' \
               f'家具有{self.furniture}'

    def add_furniture(self, item):   # item为对象

        if self.free_area >= item.area:
            self.furniture.append(item.name)   # 有空间就放入
            self.free_area -= item.area
            print(f'{item.name}存放成功！')
        else:
            print(f'{item.name}太大放不下!')

# bed = Furniture('双人床', 6)
# home = House('Beijing', 100)
# home.add_furniture(bed)
# ball = Furniture('篮球场', 500)
# home.add_furniture(ball)
# print(f'家具有{home.furniture}')
# print(home)


# 继承

class A(object):

    def __init__(self):

        self.num = 1

    def info_print(self):

        print(self.num)

class B(A):

    # def __init__(self):
    #     super().__init__()
    pass

# result = B()
# result.info_print()

class Aa(object):

    def __init__(self):
        self.info = 1

    def info_print(self):
        print(f'运用{self.info}')

class Bb(object):

    def __init__(self):
        self.info = 2

    def info_print(self):
        print(f'运用{self.info}')

class Cc(Aa, Bb):

    def __init__(self):
        self.info = 3

    def info_Cc(self):
        self.__init__()
        '有self不再传入self，初始化子类，避免被覆盖//在父类调用一次后，避免被覆盖\
                            绝对初始化子类,父类怎么调用都不变'
        print(f'运用{self.info}')

    def info_Aa(self):
        Aa.__init__(self)
        Aa.info_print(self)

    def info_Bb(self):
        Bb.__init__(self)
        Bb.info_print(self)


# 多继承
class Ccc(Cc):
    def __init__(self):
        self.__money = 2000


# cc = Cc()
# cc.info_Cc()
# cc.info_Aa()
# cc.info_Bb()
# cc.info_Cc()

# ccc = Ccc()
# ccc.info_Aa()
# print(ccc.__money) 自己都访问不到，更何况子类

# 多态
# 定义父类
class Dog(object):
    def work(self):
        print('go!')

# 定义子类
class ArmyDog(Dog):
    def work(self):
        print('catch Army!')

class DrugDog(Dog):
    def work(self):
        print('search Drug!')

# 利用子类
class Person(object):

    def work_with_dog(self, dog):
        dog.work()

# ad = ArmyDog()
# # dd = DrugDog()
# # d = Dog()
# # cc = Person()
# # cc.work_with_dog(ad)
# # cc.work_with_dog(dd)
# # cc.work_with_dog(d)



