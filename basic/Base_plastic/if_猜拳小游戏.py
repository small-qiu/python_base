# if 语句
import random
import time


player = int(input('请出拳：0--石头;1--剪刀;2--布\nYou: '))

# 判断输入
# print('i', end = '')  先sleep后print
# 只有print('i', end = '\n') 才print后sleep

time.sleep(5)
if player == 0:
    print('You input 石头，')
elif player == 1:
    print('You input 剪刀，')
else:
    print('You input 布，')

# 电脑随机输入
computer = random.randint(0,2)
time.sleep(1)
if computer == 0:
    print('Computer is 石头.')
elif computer == 1:
    print('Computer is 剪刀.')
else:
    print('Computer is 布.')
time.sleep(1)

# 判断结果
if ((player == 0) and (computer == 1)) or \
        ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('你赢了！')
elif player == computer:
    print('平局！')
else :
    print('电脑赢了！')


# 三目运算符  成立运行前，不成立运行后
aa = 10
bb = 6
cc = aa - bb if aa > bb else bb-aa
print(cc)    # cc = 4


