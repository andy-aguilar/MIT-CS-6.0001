# Get user inputs
annual_salary = int(input("Enter your annual salary: "))
portion_saved = int(input("Enter the percentage of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
r = 0.04

# Set starting points
current_savings = 0
num_months = 0

# calculate from user inputs
monthly_salary = annual_salary/12
total_down_payment = total_cost*portion_down_payment

while current_savings < total_down_payment:
    # add investment returns first
    current_savings += current_savings*(r/12)
    #add monthly salary
    current_savings += monthly_salary*portion_saved
    #go to the next month
    num_months +=1

print("Number of months:", str(num_months))
