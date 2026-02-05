height=float(input("请输入你的身高（米）："))
weight=float(input("请输入你的体重（公斤）："))
BIM=weight/(height*height)
print(f"小明的BIM指数是：{BIM}")
if BIM<18.5:
    print("过轻")
elif 18.5<BIM<=25:
    print("正常")
elif 25<BIM<=28:
    print("过重")
elif 28<BIM<=32:
    print("肥胖")
else:
    print("严重肥胖")