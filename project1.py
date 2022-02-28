#Income tax homework
#Enter gross income
#Enter number of dependants 
#calculate 20% tax rate
#Each dependant is $3000 deduction
#$10,000 deduction

deduction = 10000                                               #standard deduction set at $10,000
tax_rate = 0.20                                                 #Tax rate set at %20
dep_deduction = 3000                                            #Dependent deduction set at $3000 per dependent

print("Enter the gross income:")                                #Asks user for income
income = float(input())                                         #Stores ser input into float income

print("Enter the number of dependents:")                        #Asks user for number of dependents
dependents = int(input())                                       #Stores user input into int dependents

new_income = income - deduction - dep_deduction * dependents    #Calculates new taxable income based on all deductions
total_tax = new_income * tax_rate                               #Calculates total tax rate based on new taxable income 

print(f' The income tax is:  {total_tax:.2f} ')                 #Prints total taxes




