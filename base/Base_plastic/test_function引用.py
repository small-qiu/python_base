import file_operation  # 自定义.py文件
import os

# file_operation.copy_file("test1.docx")
file_operation.remodify_allfile(1, 'aa/bbbb')

# os.rename('test1.docx', 'testWord.docx')
# os.remove('test1[备份].docx')

# 创、删文件夹
# os.mkdir('aa')
# os.rmdir('aa')

# print(os.getcwd())  # 当前文件路径

# aa下创bb
# os.chdir('aa')
# os.mkdir('bb')

# a = os.listdir('C:/Users/Sharon/Desktop/PythonCode/Base_plastic')
# print(a)

# os.chdir('aa')
# os.rename('bb', 'bbbb')      # bb改名bbbb 无'.txt'

# 批量改名
# list_f = os.listdir('aa/bbbb')
# print(list_f)
# for i in list_f:
#     os.rename(f'aa/bbbb/{i}', f'aa/bbbb/Python{i}')    # 不能f'Python{i}'













