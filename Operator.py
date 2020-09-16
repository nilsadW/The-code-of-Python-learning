# #Integer Operation 1
# days = int(input("Enter days: "))
# months = days // 30
# days = days % 30
# print("Months = {} \nDays = {} ".format(months, days))

# Integer Operation 2
# days = int(input("Enter days: "))
# print("Months = {} \nDays = {} ".format(*divmod(days, 30)))

#salesmansalary.py            输入售卖数量和价格计算工资
basic = 1500
n = int(input("Enter the number of camera sold: "))
price = float(input("Enter the price of each camera: "))
commission = price * 0.02 * n + n * 200
total_salary = basic + commission
print("Total salary is {} ".format(total_salary))
