km= float(input("请输入打车公里数："))

if km<3.0:
    price=1+13
    print("打车费用为:{price}元")
elif km<10.0:
    price=13+(km-3)*2.3+1
    print(f"打车费用为：{price}元")
elif km>=10.0:
    price=13+7*2.3+(km-10)*2.76+1
    print(f"打车费用为：{price}元")
