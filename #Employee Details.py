#Employee Details
employee_id = int(input("Enter Employee ID: "))
basic_pay = float(input("Enter Basic Pay: "))
allowances = float(input("Enter Allowances: "))
overtime = float(input("Enter Overtime Pay: "))
incentives = float(input("Enter Incentives: "))
gross_salary = basic_pay + allowances + overtime + incentives
if  gross_salary <=20000:
    deduction = gross_salary* 0.05
elif gross_salary <= 40000:
    deduction = gross_salary* 0.10
else:
    deduction = gross_salary* 0.15
net_salary = gross_salary - deduction
print("-------------------EMPLOYEE PAYSIP---------------------")
print(f"Basic Pay     : ₹{basic_pay:.2f}")
print(f"Allowances    : ₹{allowances:.2f}")
print(f"Overtime Pay  : ₹{overtime:.2f}")
print(f"Incentives    : ₹{incentives:.2f}")
print("-" * 30)
print(f"Gross Salary  : ₹{gross_salary:.2f}")
print(f"Deduction     : ₹{deduction:.2f}")
print("-" * 30)
print(f"Net Salary    : ₹{net_salary:.2f}")