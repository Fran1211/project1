#Income tax homework
#Enter gross income
#Enter number of dependants 
#calculate 20% tax rate
#Each dependant is $3000 deduction
#$10,000 deduction

deduction = 10000                   
tax_rate = 0.20
dep_deduction = 3000

print("Enter the gross income:")
income = float(input())

print("Enter the number of dependents:")
dependents = int(input())

new_income = income - deduction - dep_deduction * dependents
total_tax = new_income * tax_rate

print(f' The income tax is:  {total_tax:.2f} ')




