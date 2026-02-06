#数学运算的进阶
#运算符
# % 取余数    相除的余数部分
# 幂运算 平方
# // 取整除   相除的整数部分，商
# i =5
# j=3
# print(i%j)
# print(i**2)
# print(i//j)
# i=2
"""
+=  i=i+1 同等于 i+=1
同理可推出
-=
*=
/=
%=
//=
**=
"""
# i+=1
# print(i)
# i**=2
# print(i)

#请取出100以内的奇数
i=0
while i<100:
    i+=1
    if i%2==1:
        continue
    print(i)
