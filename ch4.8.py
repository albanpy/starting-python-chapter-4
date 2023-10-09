#Sum of Numbers
total=0.0
num=0
while num>=0:
    num=float(input("Enter Positive number to sum|negative number to end sum:"))
    if num>0:
        total+=num
print(f'Total={total:,.2f}')
