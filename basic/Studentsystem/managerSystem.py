from student import Student

class StudentManager(object):

    def __init__(self):
        # 存储数据(存储学员对象)所用列表
        self.student_list = []

    @staticmethod
    def show_menu():  # 静态方法,括号不传参

        """显示功能函数"""
        print('请选择如下功能')
        print('1. 添加学员信息')
        print('2. 删除学员信息')
        print('3. 修改学员信息')
        print('4. 查询学员信息')
        print('5. 显示所有学员信息')
        print('6. 保存学员信息')
        print('7. 退出系统')

    def load_student(self):

        try:
            f = open('student.data', 'r')  # 不存在则报错
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()
            new_list = eval(data)   # 将文件中的字符串转换为列表格式，文件中[]不表示列表
            print(new_list)
            # 对象列表,将文件中的字典格式转换为对象，存储在self.student.list中
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()

    def add_student(self):

        name = input('Name: ')
        gender = input('Gender: ')
        tel = input('Tel: ')
        student = Student(name, gender, tel)
        # 添加对象到对象列表
        self.student_list.append(student)
        print(student)  # 打印__str__信息
        print('添加学员成功')

    def del_student(self):

        del_name = input('del_name: ')
        for i in self.student_list:
            # 访问对象属性
            if i.name == del_name:
                self.student_list.remove(i)
                print('删除学员成功')
                break
        else:
            # 循环结束都没有找到对象.name
            print('查无此人')

    def modify_student(self):

        modify_name = input('modify_name: ')
        for i in self.student_list:
            # 访问对象属性
            if i.name == modify_name:
                num = int(input('请输入修改的属性，性别1，电话2, 性别和电话3：'))
                if num == 1:
                    i.gender = input('modify_gender: ')
                elif num == 2:
                    i.tel = input('modify_tel: ')
                elif num == 3:
                    i.gender = input('modify_gender: ')
                    i.tel = input('modify_tel: ')
                print(f'Modify_student Successfully! Name:{i.name}, Gender:{i.gender},'
                      f'Tel:{i.tel}')
                break
        else:
            print('查无此人')

    def search_student(self):

        search_name = input('search_name: ')
        for i in self.student_list:
            # 访问对象属性
            if i.name == search_name:
                print(f'Name:{i.name}, Gender:{i.gender}, Tel:{i.tel}')
                break
        else:
            print('查无此人')

    def show_student(self):
        print('Name\tGender\tTel\t')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    def save_student(self):
        # 写入文件，将对象变为字典形式 实例.__dict__()
        # print(self.student_list[0].__dict__)
        # with open('student.data', 'a') as f:
        # 用'a'在删除操作保存后报错，会追加一个列表，导致下面的elva出错，elva对单列表
        with open('student.data', 'a') as f:
            # for i in self.student_list:
            #     student_dict = i.__dict__
            #     f.write(str(student_dict))
            # 没有生成list,后面elva出错

            # 将对象转换成一个一个字典，再用list封装
            new_list = [i.__dict__ for i in self.student_list]
            # 将列表格式转换为字符串存储
            f.write(str(new_list))
            f.close()
        print('保存学员信息')

    def run(self):

        # 1. 加载学员信息
        self.load_student()   # 每个打开系统前先加载系统数据，操作刷新后再保存

        # 用户需求选择
        while True:
            self.show_menu()
            menu_num = int(input('请输入需要的功能：'))
            # 根据输入执行不同功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员
                self.modify_student()
            elif menu_num == 4:
                # 查询学员
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break
