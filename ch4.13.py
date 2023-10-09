#Population
start_number=int(input("Starting number of organisms:"))
daily_increase=float(input("Average daily increase(as percentage):"))
number_day_multiply=int(input("Number of days to multiply:"))
total_number=0.0
if daily_increase>0 and daily_increase<=100:
    print("Day Approximate\t\t|Population")
    print("____________________________________")
    for day in range(1,number_day_multiply+1):
        if day==1:
            total_number=start_number
        else:
            total_number=total_number+(total_number*(daily_increase/100))
        print(f'{day}\t\t\t|{total_number:,.3f}')
    print("____________________________________")