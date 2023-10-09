#Pennies for Pay
total=0.0
salary=0.0
days=int(input("Enter number day:"))
if days>0:
    print("______________________________\n")
    print("Days\t\t|Salaries")
    print("______________________________\n")
    for pay in range(days):
         salary=(salary+(2**pay))/100#1 penny=1cent and 1 dollar=100cent so salary/100=1 dolar
         print(f'{pay+1}\t\t|${salary:,.2f}')
    total+=salary
    print("______________________________\n")
    print(f'Total salary for {days} days=${total:,.2f}')
else:
    print("Enter positive number only!!")