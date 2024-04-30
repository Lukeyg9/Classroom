exam_mark = int(input("Enter the exam mark for the student (between 1 and 100): "))

if exam_mark < 1 or exam_mark > 100:
    print("Error: Marks must be between 1 and 100")
else:
    if exam_mark < 50:
        grade = "Fail"
    elif exam_mark <= 60:
        grade = "Pass"
    elif exam_mark <= 70:
        grade = "Merit"
    else:
        grade = "Distinction"
    
    print("The grade for the exam mark {} is: {}".format(exam_mark, grade))
