#Calculating the Factorial of a Number
number=int(input("Enter a nonnegative integer(n!):"))
total=1
for n in range(1,number+1):
    total=total*n
    print(f"{n}!={total:,}")