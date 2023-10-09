speed=int(input("What is the speed of the vehicle in mph?:"))
hour=int(input("How many hours has it traveled?:"))
print("Hour\t\tDistance Traveled")
print("______________________________________")
for time in range(1,hour+1):
    distance=speed*time
    print(f"{time}\t\t{distance}")