# Technical-Debt-Management
def compute_deductions(salary):
    sss = 1200
    philhealth = (salary * 0.05) / 2
    pagibig = 100
    tax = 1875 # Assuming fixed value for simplicity

    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)


# Here is the updated code with improved readability and better variable names:

def compute_deductions(salary):
    sss_contribution = 1200
    philhealth_contribution = (salary * 0.05) / 2
    pagibig_contribution = 100
    tax_deduction = 1875  # Assuming fixed value for simplicity

    total_deductions = sss_contribution + philhealth_contribution + pagibig_contribution + tax_deduction
    net_salary = salary - total_deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss_contribution)
    print("PhilHealth Deduction:", philhealth_contribution)
    print("Pag-IBIG Deduction:", pagibig_contribution)
    print("Tax Deduction:", tax_deduction)
    print("Total Deductions:", total_deductions)
    print("Net Salary:", net_salary)

# Get user input and compute deductions
salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)