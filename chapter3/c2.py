# a=1
# b=2
# print(a==b)
# #if代码块中的内容是一个tab键或者4个空格缩进
# if a==b:#只有条件判断为Ture时才会运行if代码块的内容
#     print("a的值等于了b的值")
# else:
#     print("a的值不等于b的值")
# print("程序运行结束")    


age=50
if age<18:
    print("你还没有成年")
elif age<30:#elif是else和if的结合体，如果第一个if成立则运行if代码块
#而不会继续执行elif代码块
    print("你是个年轻人")
elif age<40:
    print("你相当成熟")

else:
    print("我无话可说")

              