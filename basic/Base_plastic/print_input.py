age, name, weight, stu_id = 18, 'QZJ', 90.5, 1

# 格式化输出  f''简单高效
print('my name is %s\nI am %d years old\nmy weight is %.2f\nmy stu_id is %03d\n' % (name, age, weight, stu_id))
print('my name is %s\nI am %s years old\nmy weight is %s' % (name, age, weight), end='...')
print(f'my name is {name},I am {age+1} years old')
print(type(name))
'''
# 1.
'My name is {},age:{}'.format('Anxc',18)
= 'My name is Anxc,age:18'
# 2.
'My name is {1},age:{0}'.format(18,'Anxc')
= 'My name is Anxc,age:18'
# 3.
'My name is{name},age:{age}'.format(name='Anxc',age=18)
 ='My name isAnxc,age:18'

'''
# 输入
number = int(input('Please input code : '))
if number == 10086:
    print('True!')
else:
    print('False!')  





