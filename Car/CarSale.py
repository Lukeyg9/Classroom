import csv

companies = []
sales = []

with open("carSale.csv", "r") as file:
    lines = file.readlines()

for x in range(0, len(lines), 2):
    company = lines[x].strip()
    companies.append(company)

    data = lines[x + 1].strip().split(',')
    sales.append(list(map(int, data)))

monthly_totals = [sum(month_sales) for month_sales in zip(*sales)]

yearly_totals = [sum(company_sales) for company_sales in sales]

for total in monthly_totals:
    print(total)

for total in yearly_totals:
    print(total)

grand_total = sum(yearly_totals)
print("Grand total:", grand_total)
