#Tuition Increase
tuition=8000 #$8000 for semister
year=1
while year<=5:
    tuition=tuition+(tuition*0.03)
    print(f'Semester tuition amount for the {year} year=${tuition:,.2f}')
    year+=1
    