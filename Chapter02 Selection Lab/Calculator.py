
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


print("\nCalculator Menu:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")


operator = input("\nChoose an operation (enter the corresponding number): ")


if operator == '1':
    result = num1 + num2
    print("The result of addition is:", result)
elif operator == '2':
    result = num1 - num2
    print("The result of subtraction is:", result)
elif operator == '3':
    result = num1 * num2
    print("The result of multiplication is:", result)
elif operator == '4':
    if num2 == 0:
        print("Error: Division by zero!")
    else:
        result = num1 / num2
        print("The result of division is:", result)
else:
    print("Invalid operator! Please choose a number between 1 and 4.")
