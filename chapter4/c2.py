#循环的跳出

i=1

while True:
    i=i+1
    print("循环正在运行"+str(i))
    if i/2==2:
        print("这个时候i等于4")
        continue
    
    if i==10:
        print("这个时候的i已经到了10")
        break#跳出循环的关键字
    #continue继续，结束本次循环，进行下次循环