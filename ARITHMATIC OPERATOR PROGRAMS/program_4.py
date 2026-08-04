
"""
Write a Python program to input basic salary. Calculate: 
HRA = 20% of Basic Salary
DA = 10% of Basic Salary
Gross Salary = Basic + HRA + DA
Display all values.
"""

salary_per_anum = 600000

hra = salary_per_anum * (20/100)
print("HRA:",hra)

da = salary_per_anum * (10/100)
print("DA:",da)

gross_salary = salary_per_anum + hra + da

print("Gross Salary:",gross_salary)