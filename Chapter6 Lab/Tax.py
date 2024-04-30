def getIncomeTax(salary):
    personal_allowance = 11850
    basic_rate_threshold = 34500
    higher_rate_threshold = 150000
    
    tax = 0
    
    if salary <= personal_allowance:
        tax = 0
    elif salary <= basic_rate_threshold:
        tax = (salary - personal_allowance) * 0.2
    elif salary <= higher_rate_threshold:
        tax = (basic_rate_threshold - personal_allowance) * 0.2 + (salary - basic_rate_threshold) * 0.4
    else:
        tax = (basic_rate_threshold - personal_allowance) * 0.2 + (higher_rate_threshold - basic_rate_threshold) * 0.4 + (salary - higher_rate_threshold) * 0.45
    
    return tax


salary = 50000
print("Income Tax for salary £{}: £{:.2f}".format(salary, getIncomeTax(salary)))
