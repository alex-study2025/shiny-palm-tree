phone_bills=[28.5,55,38,26,38]
averge=sum(phone_bills)/len(phone_bills)
diff=max(phone_bills)-min(phone_bills)
print(f"5个月的话费平均值为:{averge}元")
print(f"最高额和最低额的差值为:{diff}元")