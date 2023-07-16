def shoplist1():
    i=0
    n=1
    
    if (a>4):
        print ("Please enter a valid number from 1-4")
    if (a==1):
        for x in shopList:
            print (str(n) + ") " + x)
            n+=1
    elif (a==2):
        y = str(input("What item do you want to add to the list : "))
        shopList.append(y)
    elif (a==3):
        b=int(input("What is the order of the item you want to remove : "))
        while i < len(shopList):
            if (i==b-1):
                shopList.remove(shopList[i])
            i+=1
def greeting():
    orderNum = ["What choice do you want to take : ", " 1) View List", " 2) Add Item to Shopping List", " 3) Remove Item from Shopping List", " 4)Stop Program"]
    i=0
    while i<len(orderNum):
        print (orderNum[i])
        i+=1
shopList = ["milk", "carrots", "Eggs"]
# orderNum = ["What choice do you want to take : ", " 1) View List", " 2) Add Item to Shopping List", " 3) Remove Item from Shopping List", " 4)Stop Program", "What choice do you want to make : "]

while True:
    greeting()
    a=int(input("What choice do you want to make : "))
    if (a==4):
        break
    shoplist1()

