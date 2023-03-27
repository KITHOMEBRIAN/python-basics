def get_water_bill(num_gallons):
    bill = 1000
    bill = num_gallons / 1000
    if num_gallons < 8000:
        cost= bill*1
        print(cost)
    elif num_gallons < 22000:
        cost= bill*2
        print(cost)
    elif num_gallons < 30000:
        cost= bill*3
        print(cost)
    return bill

print(get_water_bill(20000))