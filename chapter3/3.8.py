total_repayment_amount=float(input("请输入还款总金额："))
number_of_repayment_periods=int(input("请输入还款期数："))
if number_of_repayment_periods==3:
   handling_fee= total_repayment_amount*2.50/100
   principal_repayment_per_period=total_repayment_amount/number_of_repayment_periods
   total_repayment_amount_per_period=handling_fee+principal_repayment_per_period
   print(f"每期还款金额为：{total_repayment_amount_per_period:.2f}元")
elif number_of_repayment_periods==6:
   handling_fee= total_repayment_amount*4.50/100
   principal_repayment_per_period=total_repayment_amount/number_of_repayment_periods
   total_repayment_amount_per_period=handling_fee+principal_repayment_per_period
   print(f"每期还款金额为：{total_repayment_amount_per_period:.2f}元")
elif number_of_repayment_periods==12:
   handling_fee= total_repayment_amount*8.80/100
   principal_repayment_per_period=total_repayment_amount/number_of_repayment_periods
   total_repayment_amount_per_period=handling_fee+principal_repayment_per_period
   print(f"每期还款金额为：{total_repayment_amount_per_period:.2f}元")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  