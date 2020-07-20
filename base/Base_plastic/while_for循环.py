# 1.0 while 运用，1-100和
print('1.0 while 运用，1-100和:', end='')

i = 1
result = 0
while i <= 100:
    result += i
    i += 1
print(result)

# 2.1 while 运用，偶数和
print('2.1 while 运用，偶数和:', end='')

i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1  # 不能缩进,缩进永远都没加1(死循环)，debug就知道了

print(result)

# 2.2 计数器累加求偶和
print('2.2 计数器累加求偶和:', end='')

i = 0
result = 0
while i <= 100:
    result += i
    i += 2   # 没有if语句，简单但if有逻辑
print(result)

# 3.0 break 终止所有循环，跳出循环  吃到第4个为止
print('3.0 break 终止所有循环，跳出循环  吃到第4个为止:')
i = 1
while i <= 5:
    if i == 4:
        print('不吃了\n')
        break
    print(f'吃了第{i}个')
    i += 1

# 4.0 continue 终止本次循环
print('4.0 continue 终止本次循环:')
i = 1
while i <= 5:
    if i == 3:
        print('坏了')
        i += 1    # 不加的话死循环!!!continue前必须加计算器
        continue

    print(f'吃了第{i}个')
    i += 1


# 5.1 while循环嵌套
print('5.0 while循环嵌套:')

i = 0
while i < 3:
    j = 0
    while j < 3:
        print(j)
        j += 1    # 不加死循环
    print('结束！')
    i += 1      # 不加死循环
print('总结束！')

# 5.1.1 while循环嵌套运用——5X5正方形
print('5.1.1 while循环嵌套运用——5X5正方形:\n')
i = 0
while i < 5:
    j = 0
    while j < 5:
        print('*', end='')
        j += 1
    i += 1
    print('\n')

# 5.1.2 while循环嵌套运用——三角形
print('5.1.2 while循环嵌套运用——三角形:\n')

i = 0         # i 为行号
while i < 5:
    j = 0     # j 为列号
    while j <= i:  # j和i有联动关系
        print('*', end='')
        j += 1
    i += 1
    print('\n')

# 5.1.3 9X9乘法表
print('5.1.3 9X9乘法表:\n')

i = 1
while i <= 9:
    j = 1
    while j <= i:  # j和i有联动关系
        print(f'{j}*{i}={j*i}', end='\t')
        j += 1
    i += 1
    print('\n')


# 6.1 for循环(不用计算器，但有序列）
print('6.1 for循环:')

str1 = 'string'
for i in str1:
    print(i, end='')
print('\n')

# 6.2 for + if + break + continue(同while)
print('6.2 for + if + break + continue:')

str1 = 'string'
for i in str1:
    if i == 'n':
        break    # break 终止所有循环(到n停止)，同while
    elif i == 'r':
        continue  # continue 终止本次循环(跳过r)，同while
    print(i)

# 7.1.1 while_else —— 循环正常结束之后要执行代码，和while一起用
print('7.1.1 else + while:')

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print('over!')

# 7.1.2 while_else + break  有break不执行
print('7.1.2 else + break:')

i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
else:      # 不执行
    print('5')

# 7.1.3 while_else + continue  有continue——执行
print('7.1.3 else + continue:')

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue  # !!!continue前必须加计算器
    print(i)
    i += 1
else:      # 执行
    print('5')

# 7.2.1 for_else —— 循环正常结束之后要执行代码，和for一起用,同while
# 7.2.2 for_else + break  有break不执行
# 7.2.3 for_else + continue  有continue——执行
