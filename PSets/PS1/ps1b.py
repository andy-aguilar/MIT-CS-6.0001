# Get user inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment = 0.25
r = 0.04

# set starting points
current_savings = 0
num_months = 0

# calculate from user inputs
total_down_payment = total_cost*portion_down_payment

while current_savings < total_down_payment:
    # add investment returns first
    current_savings += current_savings*r/12
    #add monthly salary
    current_savings += annual_salary*portion_saved/12
    # finish month
    num_months +=1
    #apply raise (if necessary)
    if num_months % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise
    

print("Number of months:", str(num_months))