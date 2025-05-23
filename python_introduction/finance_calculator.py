income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = income - expenses
annual_savings = (monthly_savings * 12 * (5/100)) + (monthly_savings * 12) 
print(
f"""
Your monthly savings are ${monthly_savings}.
Projected savings after one year, with interest, is: ${annual_savings}.
"""
)
