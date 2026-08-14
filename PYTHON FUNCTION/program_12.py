
"""
return is a keywordit iis uused to passed function value outside function
"""

def calculateGrossSalary(basic_salary,hra,da):
    gross_salary = basic_salary + hra + da
    print("Gross Salary:",gross_salary)
    return gross_salary
    print("helo world")

def salaryAftertax(gross_salary,percent):
    salary_after_tax = gross_salary - (gross_salary*percent/100)
    print("In hand salary:",salary_after_tax)


grosa_salary_output=calculateGrossSalary(25000,2500,2500)
salaryAftertax(grosa_salary_output,10)
