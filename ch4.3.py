#Budget Analysis
total=0.0
budget=float(input("Enter the amount that you have budgeted for a month:"))
expense=float(input("Enter each your expenses for the month or 0 to end:"))
total+=expense
while expense!=0:
    expense=float(input("Enter each your expenses for the month or 0 to end:"))
    total+=expense
print(f'Total Expenses={total:,.2f}Tsh')
if budget>expense:
    print("Amount under budget")
elif budget<expense:
     print("Amount over budget")
