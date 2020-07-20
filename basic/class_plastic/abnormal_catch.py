# 异常传递(嵌套书写见代码)
# import time   # 用于延缓，方便在cmd中中止
# try:
#     with open('test1.txt', 'r') as f:
#
#         try:
#             while True:
#                 con = f.readline()
#                 if len(con) == 0:
#                     break
#                 print(con)
#                 time.sleep(2)
#         except:
#             # cmd中按 ctrl+c 中止
#             print('意外终止')
# except:
#
#     print('不存在')



# 自定义异常
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'你输入的长度是{self.length}, 不能少于{self.min_len}'

def main():
    try:
        con = input('请输入密码： ')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)  # 抛出异常类对象=相当于打印异常对象
    except Exception as result:   # 捕获异常
        print(result)
    else:
        print('没有异常')

# main()

# 导入包 1.
import mypackage.my_model1
mypackage.my_model1.info_print1()

# 导入包 2.
from mypackage import *
my_model2.info_print2()
