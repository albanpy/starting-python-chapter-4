#Bug Collector
total=0.0
for num in range(1,6):
    bugs=float(input(f"Enter the number of bugs collected during day {num}:"))
    total+=bugs
print(f'The total number of bugs collected for five days are {total}')