N = int(input(""))

time = [] 
result = [] 

def main():
    for i in range(N):
        mission = [i for i in input("").split(" ")]
        time.append(convertion(mission[0],int(mission[1]),int(mission[2]),int(mission[3]),int(mission[4])))
        result.append(timeconvert(time[i]))
        
    for i in range(N):
        print(f"{result[i][0][0]} {result[i][0][1]} {result[i][0][2]} {result[i][0][3]} {result[i][0][4]}")

    


def timeconvert(time):
    timeconvert = [] 
    # year month day hour minute
    year = time // 31536000
    month = (time % 31536000) // 2592000
    day = ((time % 31536000) % 2592000) // 86400
    hour = (((time % 31536000) % 2592000) % 86400) // 3600
    minute = ((((time % 31536000) % 2592000) % 86400) % 3600)

    while day >= 30 and hour > 24 and minute >= 60:
        month += 1
    while hour > 24:
        day += 1
    while minute >= 60:
        hour += 1
        minute -= 60

    timeconvert.append((year,month,day,hour,minute))
    return timeconvert


def convertion(symbol,multi,d,h,s):
    sum = ((d*86400) + (h*3600)+ s)
    if symbol == '>':
        sum = sum * multi
    elif symbol == '<':
        sum = sum / multi    
    return sum







if __name__ == '__main__':
    main()



