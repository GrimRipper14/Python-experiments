# Zachary Boggs
# Taking Orders
# COP 2500C
# July 25th, 2023

#What allows for the items provided to be shortened into the format needed
def Menu(Item):
    Item = Item.split()
    if (len(Item) == 3):
        Word1 = Item[0]
        Word2 = Item[1]
        Word3 = Item[2]

        ShortWord = Word1[0] + Word2[0] + Word3[0]

        return ShortWord.upper()
    
    elif(len(Item) == 2):
        Word1 = Item[0]
        Word2 = Item[1]
        ShortWord = Word1[0] + Word2[1]

        return ShortWord.upper()
    else:
        ShortWord = Item[0][:3]

        return ShortWord.upper()
#Primary Code that is ran that the Menu Funciton is used for
def Main():
    Amount = int(input("How many items would you like to order? \n"))
    Order = []

    for i in range(Amount):
        Item = input("What is item #" + str(i+1) + "? \n")
        Order.append(Item)

        print("Your order is:")

        for i in range(len(Order)):
            Total = Menu(Order[i])
            print(Total, "-", Order[i])

Main()
