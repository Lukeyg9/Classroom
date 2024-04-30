initial_investment = float(input("Enter the initial investment amount (£): "))
target_value = float(input("Enter the target value (£): "))
interest_rate = float(input("Enter the interest rate (%): "))

investment = initial_investment
years = 0

while investment < target_value:
    investment *= (1 + interest_rate / 100)
    years += 1

print("It will take {} years for an initial investment of £{} to grow to £{} at an interest rate of {}%.".format(years, initial_investment, target_value, interest_rate))
