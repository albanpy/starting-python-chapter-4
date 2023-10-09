#Average Rainfall
year=int(input("Enter number of years:"))
total_rainfall=0.0
for num_year in range(1,year+1):
    print(f'The inches of rainfall for year of {num_year}')
    for month in range(1,13):
        rainfall=float(input(f"Enter the inches of rainfall for month of {month}:"))
        total_rainfall+=rainfall
num_month=year*12
average_rainfall=total_rainfall/num_month
print(f'Number of months:{num_month:,}')
print(f'Total inches of rainfall:{total_rainfall:,.2f} inches')
print(f'Average rainfall per month for the entire period:{average_rainfall:,.2f} inches')
