#Weight Loss
start_weight=float(input(" enter their starting weight(pounds):"))
if start_weight>=8:
    print('_______________________________')
    print('Month\t\t|Weight(Pounds)')
    print('_______________________________')
    month=1
    while month<=6:
        start_weight=start_weight-4
        print(f'{month}\t\t|{start_weight}')
        month+=1
        if start_weight<=4:
            break
    print('_______________________________')

