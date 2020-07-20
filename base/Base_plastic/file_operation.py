"""

# 打开文件
with open('test.txt', 'w') as f:
    f.write('aaa')
    f.close()

# f = open('test.txt', 'w')
# f.write('aaa')
# f.close()

# 读
with open('C:/Users/Sharon/Desktop/PythonCode/笔记.txt', 'r', encoding='UTF-8') as f:
    # print(f.readlines())
    # print(f.read())
    # for i in f:
    #     print(i)
    f.close()

# seek()
with open('test.txt', 'a+') as f:
    f.seek(2, 0)  # 'r+'下 f.seek(2, 0) = f.seek(2, 1), f.seek(2,2) 指针在结尾=读无
    con = f.read()
    print(con)


"""
import os
# 文件备份
# 输入文件名
def copy_file(old_name):

    # old_name = input('请输入正确的备份文件的名字：')

    # 备份文件的名字
    # 判断是否合格
    # old_namelist = old_name.split('.')
    # if old_namelist[-1] == 'txt':

    index = old_name.rfind('.')   # index '.'的下标
    # 出口
    if index > 0:
        postfile = old_name[index:]
        new_name = old_name[:index] + '[备份]' + postfile
        # 打开读取old_f，写入new_f
        with open(old_name, 'rb') as old_f:
            with open(new_name, 'wb') as new_f:
                # 写入数据
                # while True:
                #     con = old_f.read(1024)
                #     if len(con) == 0:
                #         break
                #     new_f.write(con)
                for i in old_f:
                    new_f.write(i)

                new_f.close()  # 关闭文件
            old_f.close()  # 关闭文件
        print('备份成功！请在文件列表中查询！')
    else:
        print('文件名有误！')
        old_name = input('请输入正确的备份文件的名字：')
        copy_file(old_name)


def remodify_allfile(flag, path):
    """批量修改path文件夹下文件名"""

    # 1 加/ 2 减
    file_list = os.listdir(path)
    print(f'修改前:{file_list}')
    os.chdir(path)   # 很重要，一定要加
    new_list = []
    for i in file_list:
        if flag == 1:
            # 加前缀
            new_name = 'Python' + i
            new_list.append(new_name)

        elif flag == 2:
            # 删前缀
            num = len('Python')
            new_name = i[num:]
            new_list.append(new_name)
        os.rename(i, new_name)
    print(f'修改后:{new_list}')


# copy_file('test.txt')
# copy_file('.txt')
# remodify_allfile(1, 'aa/bbbb')





