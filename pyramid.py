'''
 **
****
'''
x = 2
'''
for i in range(x):
    for j in range(x):
        print(' ',end = "")
    print("*"*(i+1),end = "")
    print(" ",end = "")
    print("*"*(i+1),end = "")
    x = x-1
    print("")
'''
'''
ascii = 65
x = 5 

for i in range(x):
    for j in range(i+1):
        alphabet = chr(ascii)
        print(alphabet,end = " ")
    ascii += 1
    print("")
    '''

x = 5 

for i in range(x):
    for j in range(x):
        print(" ",end = '')
    for z in range(i+1):
        print(z+1,end = ' ')
    print("")
    x = x-1

    

