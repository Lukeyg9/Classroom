def calculate_result(math_mark, english_mark, ict_mark):
    average_mark = (math_mark + english_mark + ict_mark) / 3
    
    if average_mark >= 65:
        result = "Pass"
    else:
        result = "Fail"
    
    return average_mark, result

math_mark = -1
while math_mark < 0 or math_mark > 100:
    math_mark = int(input("Enter Math exam mark (0-100): "))

english_mark = -1
while english_mark < 0 or english_mark > 100:
    english_mark = int(input("Enter English exam mark (0-100): "))

ict_mark = -1
while ict_mark < 0 or ict_mark > 100:
    ict_mark = int(input("Enter ICT exam mark (0-100): "))

average_mark, result = calculate_result(math_mark, english_mark, ict_mark)


print("\nAverage mark:", average_mark)
print("Overall result:", result)
