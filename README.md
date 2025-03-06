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


# Updated version with modular functions

def calculate_sss_contribution(salary):
    sss_contribution = 1200  
    return sss_contribution

def calculate_philhealth_contribution(salary):
    philhealth_contribution = (salary * 0.05) / 2 
    return philhealth_contribution

def calculate_pagibig_contribution():
    pagibig_contribution = 100  
    return pagibig_contribution


def calculate_tax_deduction():
    tax_deduction = 1875  # Assuming fixed value for simplicity
    return tax_deduction


def compute_deductions(salary):
    
    sss_contribution = calculate_sss_contribution(salary)
    philhealth_contribution = calculate_philhealth_contribution(salary)
    pagibig_contribution = calculate_pagibig_contribution()
    tax_deduction = calculate_tax_deduction()

    
    total_deductions = sss_contribution + philhealth_contribution + pagibig_contribution + tax_deduction
    net_salary = salary - total_deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss_contribution)
    print("PhilHealth Deduction:", philhealth_contribution)
    print("Pag-IBIG Deduction:", pagibig_contribution)
    print("Tax Deduction:", tax_deduction)
    print("Total Deductions:", total_deductions)
    print("Net Salary:", net_salary)

salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)


# Updated version with input validation and error handling

def calculate_sss_contribution(salary):
   
    sss_contribution = 1200  
    return sss_contribution

def calculate_philhealth_contribution(salary):
    
    philhealth_contribution = (salary * 0.05) / 2 
    return philhealth_contribution

def calculate_pagibig_contribution():
   
    pagibig_contribution = 100  
    return pagibig_contribution

def calculate_tax_deduction():
    
    tax_deduction = 1875  
    return tax_deduction

def compute_deductions(salary):
    
    sss_contribution = calculate_sss_contribution(salary)
    philhealth_contribution = calculate_philhealth_contribution(salary)
    pagibig_contribution = calculate_pagibig_contribution()
    tax_deduction = calculate_tax_deduction()

   
    total_deductions = sss_contribution + philhealth_contribution + pagibig_contribution + tax_deduction
    net_salary = salary - total_deductions

  
    print("Gross Salary:", salary)
    print("SSS Deduction:", sss_contribution)
    print("PhilHealth Deduction:", philhealth_contribution)
    print("Pag-IBIG Deduction:", pagibig_contribution)
    print("Tax Deduction:", tax_deduction)
    print("Total Deductions:", total_deductions)
    print("Net Salary:", net_salary)

def get_salary_input():
    while True:
        try:
            salary_input = input("Enter your monthly salary: ")
            salary = float(salary_input)  
            
            if salary <= 0:
                raise ValueError("Salary must be a positive number.") 
            return salary 

        except ValueError as e:
           
            print(f"Invalid input: {e}. Please try again.")


salary = get_salary_input()
compute_deductions(salary)

# Brief report for Documentation:

Technical debt identified
>Lack of testing of the code that leads to error.
>Refactoring the code structure

Refactoring improvements made
>Naming of variables for clarity.
>Formatting the code structure to improve the consistency.

Challenges faced & solutions
>Challenge faced is configuring out the code. 
>Finding ways to improve the maintainability and reduce its technical debt.