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
