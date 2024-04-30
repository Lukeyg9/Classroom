def find_highest(num1, num2, num3):
    highest = max(num1, num2, num3)
    return highest

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

highest_number = find_highest(num1, num2, num3)
print("The highest number is:", highest_number)
