annual_salary = float(input("Enter your annual salary: "))
semi_annual_raise = .07
ror= .04
total_cost = 1000000
percent_down_payment = .25
total_down_payment = total_cost * percent_down_payment
epsilon = 100
current_savings = 0.0
steps = 0
guess = 5000
low = 0
high = 10000

while abs(current_savings - total_down_payment) > epsilon and guess < 9999:
    guess = (high + low)/2
    guess_percentage = int(guess)/10000
    steps += 1
    test_salary = annual_salary
    current_savings = 0.0
    
    for month in range(36):
        if month != 0 and month % 6 == 0:
            test_salary += test_salary*semi_annual_raise
        current_savings+= (current_savings*ror + test_salary*guess_percentage) / 12
    if current_savings < total_down_payment:
        low = int(guess)
    else:
        high = int(guess)
        
if abs(current_savings - total_down_payment) < epsilon:
    print("Best savings rate: " + str(int(guess)/10000))
    print("Steps in bisection search: " + str(steps))
else:
    print("It is not possible to pay the down payment in three years.")
    print("Steps:", steps)