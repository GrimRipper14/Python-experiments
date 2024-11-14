# Zachary Boggs
# Menu
# COP 2500C
# July 28, 2023

def get_menu_dictionary(Filename):
    Menu = {}
    File_out = open(Filename, "r")
    Number = int(File_out.readline())
    TheMenu = ""
    for i in range(Number):
        Line = File_out.readline().split()
        Item = Line[0].capitalize()
        Price = float(Line[1])
        Menu[Item] = Price
        TheMenu += Item
        if i != Number - 1:
            TheMenu += "\n"
    print(TheMenu)
    File_out.close()
    return Menu, TheMenu


def PrintReceipt(Item, Price):
    File_out = open("receipt.txt", "w")
    TheRec = "receipt:\n"

    for Key in Item:
        TheRec += str(Key) + " @ $" + str(Item[Key]) + "\n"
    TheRec += "total: $" + str(Price)

    File_out.write(TheRec)
    File_out.close


def Main():
    print("Welcome!")

    Filename = input("What menu would you like to load?\n")
    print("Menu loaded")

    Menu, TheMenu = get_menu_dictionary(Filename)
    Item = ""
    Total = 0
    Order = {}

    while (Item != "End"):
        Item = input("What would you like to order?\n")
        Item = Item.lower().capitalize()
        if (Item in Menu):
            print("Added")
            ThePrice = Menu[Item]
            Order[Item] = float(ThePrice)
            Total += ThePrice
        elif (Item != "End"):
            print("That is not on the menu")

        print(TheMenu)

    PrintReceipt(Order, Total)
    print("Goodbye")


Main()
