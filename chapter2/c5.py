#数据类型与数字类型之间的转换
#我们声明一个数字是否能转成字符串
a = 1
b = 1.2
print(type(a))
print(type(b))
c = "我是初学者"
print(type(c))
"""
<class 'int'>
<class 'float'>
<class 'str'>
"""
#把整数转换成字符串
print(str(a))
d =str(a)
print(type(d))
print(float(a))
#浮点数转换成整数的时候，只是舍弃了小数点后的数字
print(int(b))
#注意，是不是字符串不能转换成数字？？？
#print(int(c))  #报错
e="11"
print(int(e))
#必须长得像数字的字符串才能转换成数字

#从键盘中输入 input函数代表着让用户从键盘中输入内容
# result = input()
# print("用户输入的内容是：")
# print(result)
# #字符串的相加操作
# print("您输入的内容是：" + result)
#字符串与字符串之间不能够进行减法、乘除运算
a="1111"
b="11"
# print(a-b)

#问： 当我们获取到用户从键盘中输入的内容后，这个变量是什么类型？
a=input("请输入你的内容：")
print(type(a))
#用户输入的内容默认都是字符串类型