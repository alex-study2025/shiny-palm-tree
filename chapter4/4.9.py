count = 0
for i in range(1,101):
    if(i%3==0 or i%7==0)and not(i%21==0):
        count +=1
        print(count)