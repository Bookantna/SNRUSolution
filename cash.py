from cs50 import get_float

def cash():
    cash = get_float("Change owed: ")
    while cash < 0:
        continue
    cash = cash * 100
    twentyfive = int(cash / 25) 
    ten = (cash % 25) / 10 
    five = ((cash % 25) % 10) /5 
    one = ((cash % 25) % 10) % 5
    
    sumcash = int(twentyfive + ten + five + one)
    print(sumcash)
    
cash()

