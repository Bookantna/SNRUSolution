T = int(input("Test case: "))
suchart = [] # house, suchart's money [[3, 100], [3, 100]]
house = [] # [[20, 30, 40],[20, 30, 40]]
result = [i for i in range(T)]
def check(suchart, house):
    for i in range(T):
        if int(suchart[i][0]) > len(house[i]) or int(suchart[i][0]) < len(house[i]):
            return False
        else: return True
def main():
    for i in range(T):
        x = [i for i in input("").split(" ")]
        suchart.append(x)
        y = [i for i in input("").split(" ")]
        y.sort()
        house.append(y)

    if check(suchart, house) == False:
        print('error')
    else:
        for k in range((len(suchart))):
            result[k] = 0 
            count = 0
            money = int(suchart[k][1])
            for j in range(len(house[k])):
                if money >= int(house[k][j]):
                    money -= int(house[k][j])
                    count +=1
            result[k] += count
    show()

def show():
    for i in range(T):
        print(f"Case #{i+1}:",result[i])
if __name__ == '__main__':
    main()


