#孩子身高=（父亲身高+母亲身高）*0.54
father_height=input("请输入父亲身高（米）：")
a=float(father_height)
mother_height=input("请输入母亲身高（米）：")
b=float(mother_height)
#符号的优先级，想要谁先运算，就用括号括谁
child_height=(a+b)*0.54
# print(f"孩子的身高大约是：{child_height}米")
print("孩子的身高大约是:"+ str(child_height))