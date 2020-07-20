# 切片
str1 = 'abcdefghijk'
str2 = str1[::-1]  # 逆，同列表
print(str2)
print(str1[1:4:1])  # 第3个元素-步长
print(str1[5:2:-1])  # 切片为逆必须-1步长

# 4.0 查找
# find(str,start,end)  # 从start查找到end-1,有返回初始下标，无返回-1
str3 = ' hello world and Python and Java '
print(str3.find("and", 3, 20))  # 12
print(str3.find("ands"))    # -1 ，查无
print(str3.index("and", 3, 20))  # 12
# print(str3.index("ands"))    报错
print(str3.count('and'))  # 2
print(str3.rfind("and"))  # 23
print(str3.rindex("and"))  # 23

# 5.0 修改  原字符串不变
print('5.0 修改:')
print('替分合：')
print(str3.replace('and', '&', 2))
list1 = str3.split('and', 1)
print(list1)
print('&'.join(list1))

print('大小写：')
print(str3.title())  # 首字母大写
print(str3.upper())  # 全部大写
print(str3.lower())  # 全部小写

print('删空：')
print(str3.lstrip())  # 删左空白
print(str3.rstrip())  # 删右空白
print(str3.strip())   # 删两侧空白

print('对齐：')
str4 = 'hello world'
print(str4.ljust(15, '^'))   # 左对齐
print(str4.rjust(15, '^'))   # 右对齐
print(str4.center(15, '^'))  # 中间对齐

# 6.0 判断
print('6.0 判断：')
print(str4.startswith('hello'))  # 子串开始 True or False
print(str4.endswith('rd'))  # 子串结尾 True or False
print(str4.isalpha())  # 是否纯字母 True or False
print(str4.isdigit())  # 是否纯数字 True or False
print(str4.isalnum())  # 是否纯数字、字母 True or False
print(str4.isspace())  # 是否空白 True or False

