# Step 1: Create two lists
companies = []
sales = []

# Step 2: Read all the lines from carSale.csv file
with open("carSale.csv", "r") as file:
    lines = file.readlines()

# Step 3: Loop through the lines and populate the lists
for x in range(0, len(lines), 2):
    # Extract company name
    company = lines[x].strip()
    companies.append(company)

    # Extract sales data line and convert it into a numeric list
    data = lines[x + 1].strip().split(',')
    sales.append(list(map(int, data)))

# Step 4: Calculate statistics
# 1. Sum of cars sold in each month
monthly_totals = [sum(month_sales) for month_sales in zip(*sales)]

# 2. Total yearly sales by each manufacturer
yearly_totals = [sum(company_sales) for company_sales in sales]

# Printing the results
for total in monthly_totals:
    print(total)

for total in yearly_totals:
    print(total)

# Grand total
grand_total = sum(yearly_totals)
print("Grand total:", grand_total)
