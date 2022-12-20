N = int(input("Number: "))
N = 2
'''
0123456789
XXXXXXXX/\XXXX/\
XXX/\XX/OO\XX/OO\
/\/OO\/OOOO\/OOOO\
    '''

def main():
    con = [i for i in input("").split(" ")]
    if (len(con) > N or len(con) < N):
        print("Error")
    else:    
        height = highest(con)
        mountain(con,height,N)

def highest(con):
    highest = 0
    for i in range(len(con)):
        if con[i] > highest:
            highest = con[i]
    return highest

def mountain(con,height,N):
    for i in range(height):
        for j in range(N):
            for k in range(con[j]):
                if i + k == height-1:
                    print("/",end = '')
                else:
                    print(" ",end= '')
            k = con[j] -1
            while k >=0:
                if i + k == height-1:
                    print("\\",end = '')
                else:
                    print(" ",end= '')
                k -=1
        print("")



            


if __name__ == '__main__':
    main()